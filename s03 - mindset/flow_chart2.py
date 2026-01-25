def move(file):
    pass

def is_project(file):
    pass

def is_media(file):
    pass

def not_valid(file):
    pass

files = None

for file in files:
    if not_valid(file):
        move(file)

    elif is_media(file):
        move(file)

    elif is_media(file):
        move(file)
    else: move("archive")