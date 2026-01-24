import os
import shutil

src = "path/files"
dst_folder = 'path/files/TextFiles'

os.makedirs(dst_folder, exist_ok=True)

for file_name in os.listdir(src):
    full_file_path = os.path.join(src, file_name)
    print("start")
    if os.path.isfile(full_file_path) and file_name.endswith('.txt'):
        print("if statement has checked")
        dest_path = os.path.join(dst_folder, file_name)
        shutil.move(full_file_path, dest_path)