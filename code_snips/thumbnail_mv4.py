import ffmpeg

in_file = "/Users/juliaguimiot/Downloads/11a.m4v"
# in_file="output.mp4"
out_file = "thumbnail.jpg"
time = 0.1

meta = ffmpeg.probe(in_file)
width = meta["streams"][0].get("width", 1000)
height = meta["streams"][0].get("height", None)

print(meta["streams"][0])
def get_timestamp(meta, max_time=60.0):
    for stream in meta["streams"]:
        if "duration" in stream:
            # this will grab a thumbnail 20% thru the video
            video_duration = float(stream["duration"])
            if (
                video_duration > max_time
            ):  # do not go too far into video it is a performance hit
                return max_time
            else:
                return video_duration * 0.2  # 20% in as requested by product


timestamp = get_timestamp(meta)

breakpoint()
ffmpeg.input(in_file, ss=timestamp).filter('scale', width, height).output(out_file, frames=1).run()


# ffmpeg.input(in_filename, ss=time).filter("scale", width, -1).output(out_filename, vframes=1).run()

# ffmpeg.input(in_filename, ss=time).filter('scale', width, -1).output(out_filename, vframes=1).run()

# .overwrite_output()
# capture_stdout=True, capture_stderr=True
