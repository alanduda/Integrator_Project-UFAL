def readFile(filename):
    file = open(filename, 'r')
    matriz = []

    text = file.readlines()

    for i in range(len(text)):
        matriz.append((text[i].split()))

    file.close()

    return matriz
