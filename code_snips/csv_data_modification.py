import csv
import json

# Opening JSON file to make sure we handle special case Users
with open('testing_report_counts.json') as json_file:
    data = json.load(json_file)
    with open('testing_report_counts.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        for key, value in data.items():
            for key2, value2 in value.items():
                if key2 != "rwe" and value2 > 0:
                    writer.writerow([key, key2, value2])


        # writer.writerow(data.values())



    # # process the data from the csv file so that we get a list of names and new emails
    # with open('/Users/juliaguimiot/Downloads/eon_users.csv', mode='r') as infile:
    #     reader = csv.reader(infile)
    #     users=[]
    #     for row in reader:
    #         name = "{} {}".format(row[0], row[1])
    #         email = "{}".format(row[2])
    #         if email in data["non_standard"]:
    #             new_email = data["non_standard"][email]["new_email"]
    #             users.append([name, new_email])
    #             continue
    #         if email in data["no_change"]:
    #             continue
    #         new_email = email.replace("eon", "rwe")
    #         users.append([name, new_email])

    #     # write the data to a csv file
    #     with open('eon_to_rwe_users.csv', mode='w') as outfile:
    #         writer = csv.writer(outfile)
    #         writer.writerows(users)
