import os
import requests
import json


def downloadData(dir_work, dataset_txt, attrs):

    os.chdir(dir_work)
    file_dataset_list = open(dataset_txt)

    urlBase, *dataset_list = list(map(lambda x: x.replace(
        '\n', ''), file_dataset_list.readlines()))
    file_dataset_list.close()

    for dataset in dataset_list:
        data_main_raw = download_data(
            f'{urlBase}/{dataset}_main.txt')

        data_main = dict(
            list(map(lambda x: filter(lambda x: len(x) > 0, x.split(' ')), extract_info(data_main_raw))))

        for key_d in data_main.keys():
            if key_d in attrs:
                if key_d != 'name' and key_d != 'code':
                    data_main[key_d] = extract_lines_data(extract_info(
                        download_data(f'{urlBase}/{data_main[key_d]}')))
                else:
                    data_main[key_d] = extract_info(
                        download_data(f'{urlBase}/{data_main[key_d]}'))

        file_data_save = open(f'{dataset}.json', 'w+')
        json.dump(data_main, file_data_save)
        file_data_save.close()
        print(f'{dataset}: Salvo!')


def download_data(url):
    return requests.get(url=url).text


def extract_info(data):

    i, data_l = 0, data.split('\n')
    while i < len(data_l) and data_l[i][0] == '#':
        i += 1

    if i >= len(data_l):
        return None

    return list(map(lambda x: x.replace('\n', ''), data_l[i:len(data_l) - 1]))


def extract_lines_data(data):

    matrix = []
    for i_matx, line in enumerate(data):

        j, line_arr = 0, []
        for i in range(len(line)):
            if line[i] == ' ':
                if i > j:
                    line_arr.append(float(line[j:i]))
                j = i + 1

            i += 1
        matrix.append(line_arr)

        if j < len(line):
            line_arr.append(float(line[j:len(line)]))

    return matrix


downloadData('./data', 'list_dataset.txt',
                     ['name', 'dist', 'code'])