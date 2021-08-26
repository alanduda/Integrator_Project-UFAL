
def readFile(filename):
    arq = open(filename, 'r')  # abre o arquivo
    texto = []  # declaro um vetor
    matriz = []  # declaro um segundo vetor
    texto = arq.readlines()  # quebra as linhas do arquivo em vetores
    # print("vetor texto -> ", texto)  # aqui eu mostro
    # print("")

    for i in range(len(texto)):  # esse for percorre a posições dp vetor texto
        # aqui eu quebro nos espasos das palavras
        matriz.append(texto[i].split())

    # print("vetor matriz -> ", matriz)  # mostra o vertor com um conjunto de vetores
    # # print("")
    # for i in range(len(texto)):  # mostra quedrando em linhas
    #     print(matriz[i])

    arq.close()  # comando para fechar o arquivo

    return matriz
