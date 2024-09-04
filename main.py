import os
import shutil
import glob

# creating a dictionary mapping a list of folder with the file types their can contain.
folder_extensions = {
    "Documents": [".docx", ".pdf", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Code": [".py", ".js", ".html", ".css", ".java"],
    "Archives": [".zip", ".rar", ".tar.gz", ".7z"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Scripts": [".sh", ".bat", ".ps1"],
    "Web": [".html", ".css", ".js", ".php"]
}

# initialize the download path where we want to rearrange the files.
base_path = "/Users/stationx/Downloads"

# check if the folder exists if not create them
for folders in folder_extensions.keys():
    folder_path = os.path.join(base_path, folders)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# find the files and move them to the appropriate folders
for folders, exts in folder_extensions.items():
    for ext in exts:
        files = glob.glob(os.path.join(base_path, f"*{ext}"))

        for file in files:
            shutil.move(file, os.path.join(base_path, folders))

