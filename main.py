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
moved_files = []

if os.path.isdir(downloads_folder):

    downloads_folder_files = os.listdir(downloads_folder)

    if len(downloads_folder_files) > 0:

        for file in downloads_folder_files:

            downloads_file_full_name = os.path.join(downloads_folder, file)

            if os.path.isfile(downloads_file_full_name):

                file_name, extension = os.path.splitext(file)

                if extension in allowed_image_extensions:
                    
                    pictures_file_full_name = os.path.join(pictures_folder, file)

                    if os.path.exists(pictures_file_full_name):
                        failed_to_move_files.append(file)
                        continue

                    try:
                        os.rename(downloads_file_full_name, pictures_file_full_name)
                        moved_files.append(f'{file} moved to {pictures_folder}')
                    except:
                        failed_to_move_files.append(f'{file} failed to move to {pictures_folder}')
                        continue

                elif extension in allowed_video_extensions:
                    
                    videos_file_full_name = os.path.join(videos_folder, file)

                    if os.path.exists(videos_file_full_name):
                        failed_to_move_files.append(file)
                        continue

                    try:
                        os.rename(downloads_file_full_name, videos_file_full_name)
                        moved_files.append(f'{file} moved to {videos_folder}')
                    except:
                        failed_to_move_files.append(f'{file} failed to move to {videos_folder}')
                        continue

                elif extension in allowed_music_extensions:
                    
                    music_file_full_name = os.path.join(music_folder, file)

                    if os.path.exists(music_file_full_name):
                        failed_to_move_files.append(file)
                        continue

                    try:
                        os.rename(downloads_file_full_name, music_file_full_name)
                        moved_files.append(f'{file} moved to {music_folder}')
                    except:
                        failed_to_move_files.append(f'{file} failed to move to {music_folder}')
                        continue

                elif extension in allowed_document_extensions:
                    
                    document_file_full_name = os.path.join(documents_folder, file)

                    if os.path.exists(document_file_full_name):
                        failed_to_move_files.append(file)
                        continue

                    try:
                        os.rename(downloads_file_full_name, document_file_full_name)
                        moved_files.append(f'{file} moved to {documents_folder}')
                    except:
                        failed_to_move_files.append(f'{file} failed to move to {documents_folder}')
                        continue
                else:
                    failed_to_move_files.append('{file} failed to move: Invalid File Extension')

    print('************************')
    print('** MOVED FILES **')
    print('************************')
    
    for moved_file in moved_files:
        print(moved_file)

    print("\n" + str(len(moved_files)) + " files moved!! ")

    print("\n")
    print('************************')
    print('** FAILED MOVE FILES **')
    print('************************')
    print("\n")
    print(str(len(failed_to_move_files)) + " files failed to be moved!! ")

    for failed_move_file in failed_to_move_files:
        print(failed_move_file)

else:
    print("Invalid Downloads Folder")
