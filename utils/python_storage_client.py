import logging
from google.cloud import storage
import settings



def grab_gcs_file(client, new_filename, directory, namespace, content_type='text/csv'):
    """ grab the files from gcs"""
    filename = "{}/{}".format(directory, new_filename)
    logging.info('grab_gcs_file{}: grabbing gcs client handle {}'.format(namespace, filename))
    bucket = client.get_bucket(settings.GCS_BUCKET)  # TODO 'user_project' attr to seperate out our buckets
    # TODO: I have seen a 'GatewayTimeout: 504' on this get_bucket call
    # if not blob_exists(bucket, filename):
    blob = storage.blob.Blob(filename, bucket, chunk_size=9 * 1024 * 1024)  # set chunk size to just under 10 megs Other Sizes I tried:256,1024,262144
    blob.content_type = '{}; charset=utf-8'.format(content_type)
    blob.content_encoding = 'UTF-8'
    # else:
    #     blob = bucket.blob(filename)

    return blob

def create_zip_archive(client, base_upload_dir, zip_filename, project_types, namespace):
    storage_bucket = client.get_bucket(settings.GCS_BUCKET)
    files = client.list_blobs(settings.GCS_BUCKET, prefix=base_upload_dir, delimiter=None)

    filenames_in_zip = []  # used to prevent dupes
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for file in files:
            unique_project_type_names = []
            for project_type in project_types:
                (project_type_name, unique_project_type_names) = sanitize_name(project_type.name, unique_project_type_names, project_type.key.id())
                cl_data = "{}_{}.csv".format(project_type_name, "checklist_data")
                defects = "{}_{}.csv".format(project_type_name, "defects")
                projects = "{}_{}.csv".format(project_type_name, "projects")
                if cl_data in file.name or defects in file.name or projects in file.name:
                    if file.name not in filenames_in_zip:
                        logging.info("data_downloads:{}:[{}]create_zip_archive adding file: {} to zip {}".format(namespace, datetime.today().strftime('%H:%M:%s'), file.name, zip_filename))
                        # csv_buffer = io.TextIOWrapper(io.BytesIO(), encoding='utf-8', newline='\n')
                        # logging.info("data_downloads: {} Downloading Bucket[{}] Blob [{}]".format(namespace, settings.GCS_BUCKET, file.name))
                        blob = storage.Blob(file.name, storage_bucket)
                        csv_buffer = blob.download_as_string(client)  # https://googleapis.dev/python/storage/1.22.0/blobs.html
                        zip_file.writestr(file.name, csv_buffer)
                        filenames_in_zip.append(file.name)
                    else:
                        logging.warning("data_downloads:{}:[{}]create_zip_archive file: {} already in zip buffer {}".format(namespace, datetime.today().strftime('%H:%M:%s'), file.name, zip_filename))

    logging.info('data_downloads{}:[{}]create_zip_archive about to write zip_filename: {} to gcs storage'.format(namespace, datetime.today().strftime('%H:%M:%s'), zip_filename))
    blob = storage.blob.Blob(zip_filename, storage_bucket, chunk_size=9 * 1024 * 1024)
    blob.upload_from_file(zip_buffer, rewind=True)
    return blob.size