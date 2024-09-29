import os
import shutil

# Specify the path to the source folder where the files are located
source_folder = r'path to folder'

# Specify the path to the destination folder where you want to copy the mp4 files to
destination_folder = r'path to folder'

# Make sure the destination folder exists, if not, create it
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Go through all the files in the source folder
for filename in os.listdir(source_folder):
    full_file_path = os.path.join(source_folder, filename)

    # Check that it's a file (exclude folders)
    if os.path.isfile(full_file_path):
        # If the file is .mp4, copy it
        if filename.endswith('.mp4'):
            try:
                shutil.copy(full_file_path, destination_folder)
                print(
                    f'File {filename} successfully copied into {destination_folder}')
            except Exception as e:
                print(f'Error when copying a file {filename}: {e}')
        else:
            # Skip files that aren't .mp4
            print(f'File {filename} omitted as it is not .mp4')
    else:
        # Skip non-file objects (as example folders)
        print(f'{filename} is not a file, skip it')

print("Copying is complete")
