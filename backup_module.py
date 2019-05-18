import os
import time
from zipfile import ZipFile
"""
    Module makes a backup copy of chosen directories. I tried to make it cross-platform.
    Meant to be run from command line, but i wanna make it more like a module for importing.
    Maybe i should have used tuples.
"""

# list of source dirs for archiving
source = ['C:'+os.sep+'Projects'+os.sep+'Android', ]

# backup dir
target_dir = 'D:'+os.sep+'PyBackup'

# for subdir name
today_dir = target_dir + os.sep + time.strftime('%d%m%Y')


def make_backup_dir(target=target_dir):
    # checks and creates backup dir
    if not os.path.exists(target):
        os.mkdir(target)
        print("directory created: ", target)


def make_today_dir(today=today_dir):
    # checks and creates backup dir
    if not os.path.exists(today):
        os.mkdir(today)
        print("directory created: ", today)


def make_full_path(today=today_dir):
    # commenting, creates full path
    comment = input("make a note ->")
    if len(comment) == 0:
        archive = today + os.sep + time.strftime('%H%M%S') + '.zip'
    else:
        archive = today + os.sep + time.strftime('%H%M%S') + '_' + comment.replace(' ', "_") + '.zip'
    return archive


def write_dir_to_zip(zipfile, directory):
    """recursively writes all dirs and files in 'zipfile' from 'dir'"""
    zipfile.write(directory)
    if os.path.isdir(directory):
        sub_dir_list = []
        for item in os.listdir(directory):
            sub_dir_list.append(directory + os.sep + item)
        for item in sub_dir_list:
            if os.path.isdir(item):
                write_dir_to_zip(zipfile, item)
            else:
                zipfile.write(item)


def archive_main():
    # prepare directories
    make_backup_dir()
    make_today_dir()
    # make full archive path
    archive_path = make_full_path()

    # make an archive, write items in it, and finish
    archive = ZipFile(archive_path, 'x')
    for item in source:
        write_dir_to_zip(archive, item)
    archive.close()
    print("new backup was added: ", archive_path)


if __name__ == '__main__':
    archive_main()
else:
    pass  # пока что
