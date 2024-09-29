from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

# Function for extending the video duration with even-numbered repeat playback


def extend_video_duration_with_reverse(input_path, output_path, target_duration):
    # Uploading a video file
    clip = VideoFileClip(input_path)

    # Determining the current video duration
    current_duration = clip.duration

    # Calculating how many times to repeat the video
    repeat_count = int(target_duration // current_duration) + 1

    # Create a list of video clips where even-numbered repetitions are played backwards
    clips = []
    for i in range(repeat_count):
        if i % 2 == 0:
            # The odd ones (by index) remain as they are
            clips.append(clip)
        else:
            # Even (by index) is played backward
            reversed_clip = clip.fx(vfx.time_mirror)
            clips.append(reversed_clip)

    # Merge all clips into one
    extended_clip = concatenate_videoclips(clips)

    # Trimming to exact duration (if necessary)
    final_clip = extended_clip.subclip(0, target_duration)

    # Saving a new video
    final_clip.write_videofile(
        output_path,
        codec="libx264",
        preset="slow",
        bitrate="5100k",
        threads=4,
        ffmpeg_params=["-crf", "18"]
    )

    final_clip.write_videofile(output_path, codec="libx264")

    clip.close()
    final_clip.close()


# Example of use:
# input_video = "input_video.mp4"  # original video
# time-lapse video
# output_video = "path to file"
# target_duration = 2  # desired duration (2 seconds)

# extend_video_duration_with_reverse(input_video, output_video, target_duration)
