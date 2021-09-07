
import os
import json


def dataload(file_name):

    os.chdir('./')

    file = json.load(open(f'data/{file_name}.json'))

    return file
