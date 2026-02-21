import os
import shutil
import pandas as pd


def organize_file(file_data):
    df = pd.DataFrame(file_data)
    df.to_excel("File_Summery_Report.xlsx", index=False)

    for item in file_data:
        category = item['category']
        filename = item['filename']

        if not os.path.exists(category):
            os.makedirs(category)

        shutil.move(filename, os.path.join(category, filename))

    print("Organization ended")