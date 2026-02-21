import os
from brain_center import process_content
from organizer import organize_file


def run_project():
    source_folder = "./my_notes"

    all_results = []

    if not os.path.exists(source_folder):
        print("Please create the my_note folder")
        return

    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_folder, filename)

            with open(file_path, 'r', encoding='utf-8') as  f:
                content = f.read()

            print(f"Processing: {filename}...")
            category, summery = process_content(content)

            all_results.append({
                "filename": file_path,
                'category': category,
                "summery": summery
            })
    if all_results:
        organize_file(all_results)

    else:
        print("No txt file founded")


if __name__ == "__main__":
    run_project()