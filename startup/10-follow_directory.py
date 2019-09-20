from issgoogletools.initialize import get_gdrive_service
from issgoogletools.gdrive import folder_exists_in_root, \
    folder_exists, create_folder, upload_file
from glob import glob



def get_file_list(dir):
    return glob(dir)


def get_new_file_list(old, new):
    return list(set(new) - set(old))
