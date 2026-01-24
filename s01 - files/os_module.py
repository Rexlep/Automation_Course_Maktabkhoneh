import os
import shutil

path = 'home/documents/files'
dire = 'home'
file = 'test/second_folder/first_names.txt'

first_part = 'fake/second_folder'
last_part = 'first_names.txt'

print(os.getcwd())
print(os.listdir())

# os.mkdir("del.py")

# os.rename('test/first_folder/first_text/new_name.txt', 'test/first_folder/first_text/first_names.txt')

# os.rename('test/first_folder/first_text', 'test/first_folder/text')

# os.remove('first_names.txt')

# os.rmdir('test/first_folder/text')

# shutil.rmtree('test/first_folder/text')

# os.makedirs('home/documents/files', exist_ok=False)

print(os.path.exists(path))
print(os.path.isdir(dire))
print(os.path.isfile(file))

full_path = os.path.join(first_part, file)
print(full_path)