import os

downloads_folder = r"/home/philane/Downloads/"

pictures_folder = r"/home/philane/Pictures"
videos_folder = r"/home/philane/Videos"
music_folder = r"/home/philane/Music"
documents_folder = r"/home/philane/Documents"

allowed_image_extensions = [".jpg", ".png", ".jpeg", ".svg"]
allowed_video_extensions = [".mp4", ".mkv"]
allowed_music_extensions = [".mp3", ".wav"]
allowed_document_extensions = [".mp3", ".wav"]

failed_to_move_files = []
moved_images = []

if os.path.isdir(downloads_folder):

    downloads_folder_files = os.listdir(downloads_folder)

    if len(downloads_folder_files) > 0:

        for file in downloads_folder_files:

            downloads_file_full_name = os.path.join(downloads_folder, file)
            pictures_file_full_name = os.path.join(pictures_folder, file)

            if os.path.isfile(downloads_file_full_name):

                file_name, extension = os.path.splitext(file)

                if extension in allowed_image_extensions:
                    
                    if os.path.exists(pictures_file_full_name):
                        failed_to_move_files.append(file)
                        continue

                    try:
                        #os.rename(downloads_file_full_name, pictures_file_full_name)
                        moved_images.append(file)
                    except:
                        failed_to_move_files.append(file)
                        continue



    print(str(len(moved_images)) + " files moved")
else:
    print("Invalid Downloads Folder")
