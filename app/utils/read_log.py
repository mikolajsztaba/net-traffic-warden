import os
import glob

def get_latest_file_content(directory):
    files = glob.glob(os.path.join(directory, '*'))
    if not files:
        return None

    latest_file = max(files, key=os.path.getmtime)

    with open(latest_file, 'r') as file:
        return file.read()
