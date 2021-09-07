from helpers.saveFile import saveJson
from tests.mainNN import mainNN
from tests.mainBF import mainBF

from helpers.dataload import dataload
from timeit import default_timer as timer

def run(fileName):
    dataset = dataload(fileName)

    matrix = dataset['dist']
    
    #Em caso de uso do dataset usca312.
    if(fileName == 'usca312'):
        arr = []
        for i in dataset['dist']:
            arr.extend(i)

        l = 312
        data = [[] for i in range(l)]
        for i in range(len(arr)):
            data[i // l].append(arr[i])
        dataset['dist'] = data
        matrix = data


    nn_st = timer()
    nn_dist, nn_path = mainNN(matrix, source=0)
    nn_et = timer()

    # bf_st = timer()
    # bf_dist, bf_path = mainBF(matrix,source=0)
    # bf_et = timer()


    dataResult = {
        # 'bruteforce':{'dist':bf_dist, 'path':bf_path, 'time':bf_et - bf_st},
        'nearest-neighbor':{'dist':nn_dist, 'path':nn_path, 'time':nn_et - nn_st}
    }

    saveJson(dataResult, fileName)
    print(f'Result file {fileName} has been saved.\n')
    # print('brute-force: custo =>',dataResult['bruteforce']['dist'],'\n')
    print('nearest-neighbor: custo =>',dataResult['nearest-neighbor']['dist'],'\n')
   

run('lau15')

