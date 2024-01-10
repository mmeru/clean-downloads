import os
import shutil

# Set the source and destination folders
downloads_folder = os.path.expanduser("~/Downloads")  # Path to Downloads folder
pictures_folder = os.path.expanduser("~/Pictures")    # Path to Pictures folder
music_folder = os.path.expanduser("~/Music")          # Path to Music folder
videos_folder = os.path.expanduser("~/Videos")        # Path to Videos folder
documents_folder = os.path.expanduser("~/Documents")  # Path to Documents folder

# Ensure the destination folders exist
for folder in [pictures_folder, music_folder, videos_folder, documents_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# List of common image, music, video, and document file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
music_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.m4a']
video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.m4v', '.webm']
document_extensions = ['.txt', '.pdf', '.docx', '.xlsx', '.pptx', '.csv']

# Function to move files based on extension
def move_file(source_path, destination_folder):
    filename = os.path.basename(source_path)
    destination_path = os.path.join(destination_folder, filename)

    # Check if a file with the same name already exists in the destination folder
    i = 1
    while os.path.exists(destination_path):
        base_name, ext = os.path.splitext(filename)
        new_filename = f"{base_name}_{i}{ext}"
        destination_path = os.path.join(destination_folder, new_filename)
        i += 1

    # Move the file to the destination folder
    shutil.move(source_path, destination_path)
    print(f"Moved: {filename} to {destination_path}")

# Loop through the files in the Downloads folder
for filename in os.listdir(downloads_folder):
    source_path = os.path.join(downloads_folder, filename)

    # Check if the file is an image
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        move_file(source_path, pictures_folder)

    # Check if the file is a music file
    elif any(filename.lower().endswith(ext) for ext in music_extensions):
        move_file(source_path, music_folder)

    # Check if the file is a video file
    elif any(filename.lower().endswith(ext) for ext in video_extensions):
        move_file(source_path, videos_folder)

    # Check if the file is a document file
    elif any(filename.lower().endswith(ext) for ext in document_extensions):
        move_file(source_path, documents_folder)

print("All image, music, video, and document files have been moved to their respective folders.")
