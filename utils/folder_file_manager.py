import os
import ntpath


def get_index_from_file_path(path):

    try:
        file_parent_path, file_name = ntpath.split(path)
        base_name, extension = os.path.splitext(file_name)
        index = int(base_name[base_name.rfind("_") + 1:])
    except Exception as e:
        file_name = ""
        index = ""
        print(e)

    return file_name, index


def load_text(filename):

    if os.path.isfile(filename):
        file = open(filename, 'r')
        text = file.read()
        file.close()
    else:
        text = ''

    return text


def save_file(content, filename, method):

    file = open(filename, method)
    file.write(content)
    file.close()

    return
