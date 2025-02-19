import os
import shutil
from datetime import datetime


def backup_directory(source, destination):
    # Create a timestamp to name the backup folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(destination, f"backup_{timestamp}")

    # Create the backup directory if it does not exist
    os.makedirs(backup_path, exist_ok=True)

    # Copy all files and subdirectories from source to the backup folder
    shutil.copytree(source, backup_path, dirs_exist_ok=True)
    print(f"Backup of {source} completed successfully. Folder: {backup_path}")


if __name__ == '__main__':
    # Specify the source directory (folder to backup)
    source_directory = "C:\\path\\to\\source_folder"
    # Specify the destination directory where the backup folder will be created
    destination_directory = "C:\\path\\to\\backup_folder"
    backup_directory(source_directory, destination_directory)
