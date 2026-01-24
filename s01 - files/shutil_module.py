import shutil

src = "test\\first_folder\\first_names.txt"
dst = "test\\second_folder\\first_names_copy.txt"

shutil.move(src, dst)
shutil.copy(src, dst)