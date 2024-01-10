# Clean Downloads Script

This Python script is designed to help you organize files in your "Downloads" folder by categorizing and moving them into specific folders based on their file extensions. It utilizes the `os` and `shutil` libraries for file and folder operations. Below is a detailed explanation of how the script works and how to use it.

## Usage

Before using the script, you should ensure you have Python installed on your system.

1. **Set the Source and Destination Folders**: In the script, you need to specify the source folder (`downloads_folder`) and the destination folders for different file types (`pictures_folder`, `music_folder`, `videos_folder`, `documents_folder`). You can change these folder paths according to your system's file structure.

   ```python
    downloads_folder = os.path.expanduser("~/Downloads")  # Path to Downloads folder
    pictures_folder = os.path.expanduser("~/Pictures")    # Path to Pictures folder
    music_folder = os.path.expanduser("~/Music")          # Path to Music folder
    videos_folder = os.path.expanduser("~/Videos")        # Path to Videos folder
    documents_folder = os.path.expanduser("~/Documents")  # Path to Documents folder
    ```

2. **Ensure Destination Folders Exist**: Before moving files, the script checks if the destination folders exist. If not, it creates them.

    ```python
    for folder in [pictures_folder, music_folder, videos_folder, documents_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    ```

3. **Define File Extensions**: The script lists common file extensions for images, music files, video files, and document files.

    ```python
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    music_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.m4a']
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.m4v', '.webm']
    document_extensions = ['.txt', '.pdf', '.docx', '.xlsx', '.pptx', '.csv']
    ```

4. **Move Files to Respective Folders**: The script defines a function `move_file` to move files based on their extensions. It checks if a file with the same name exists in the destination folder and appends a number to the filename if necessary to avoid overwriting.

    ```python
    def move_file(source_path, destination_folder):
        # ...
        # Code for moving files
        # ...
    ```

5. **Loop Through Files in Downloads Folder**: The script then loops through the files in the "Downloads" folder, checks their extensions, and moves them to the appropriate destination folder.

    ```python
    for filename in os.listdir(downloads_folder):
        source_path = os.path.join(downloads_folder, filename)

        # Check file extension and move to the corresponding folder
        # ...
    ```

6. **Completion Message**: After all the files are sorted, a completion message is displayed.

    ```python
    print("All image, music, video, and document files have been moved to their respective folders.")
    ```

## Execution

To use the script, you can:

1. Copy and paste it into a Python (.py) file.
2. Modify the source and destination folder paths as needed.
3. Run the script using a Python interpreter.

The script will then automatically organize the files in your "Downloads" folder into their respective categories, making it easier for you to locate and manage your files.
