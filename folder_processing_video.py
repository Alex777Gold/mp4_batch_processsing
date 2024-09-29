import os
# Import a function from another file
from duration_video import extend_video_duration_with_reverse


def process_all_videos_in_folder(source_folder, destination_folder, target_duration):
    '''Function to process all video files in a folder'''
    # Make sure the destination folder exists, if it doesn't, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Go through all the files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.mp4'):
            input_video_path = os.path.join(source_folder, filename)
            output_video_path = os.path.join(
                destination_folder, f'extended_{filename}')

            print(f'Video processing: {filename}')

            # Calling a function for video processing from the file
            extend_video_duration_with_reverse(
                input_video_path, output_video_path, target_duration)

            print(
                f'Video {filename} successfully processed and saved as {output_video_path}')


if __name__ == "__main__":
    # Path to the source folder with the video files
    source_folder = r'path to folder'

    # Folder for saving results
    destination_folder = r'path to folder'

    # Desired duration for all videos
    target_duration = 2  # For example, 2 seconds

    # Processing all videos in a folder
    process_all_videos_in_folder(
        source_folder, destination_folder, target_duration)
