#!/usr/bin/env python3

import os
import time
import schedule
import importlib.util


package_recs = 'schedule'

spec = importlib.util.find_spec(package_recs)
if spec is None:
    print(package_recs +" is not installed")
    exit

download = os.path.join(os.path.expanduser('~'), 'Downloads')

def check_folder(download, filetype):
    _path = os.path.join(download, filetype)
    if not os.path.exists(_path):
        os.makedirs(_path)


def move_files(download, filetype):
    _path = os.path.join(download, filetype)
    _files = os.listdir(download)
    for f in _files:
        if f.endswith('.' + filetype):
            f_path_ori = os.path.join(download, f)
            f_path_tar = os.path.join(_path, f)
            os.rename(f_path_ori, f_path_tar)


def check_for_downloads():
    filetypes = []

    for f in os.listdir(download):
        if f.startswith('.'):
            pass
        elif '.' in f:
            if f.split('.')[1] in filetypes:
                pass
            else:
                filetypes.append(f.split('.')[1])


    for filetype in filetypes:
        check_folder(download, filetype)
        move_files(download, filetype)

schedule.every().hour.do(check_for_downloads)

while True:
    schedule.run_pending()
    time.sleep(1)
