import sys

def nearestNeighbor(matrix, source):
    """
    NearestNeighbor TSP algorithm
    https://pt.wikipedia.org/wiki/Algoritmo_do_vizinho_mais_pr%C3%B3ximo
    Args:
        graph: adjacency matrix
        source: starting point
 
    Examples:
        >>> import numpy as np
        >>> graph = np.array([[  0, 300, 250, 190, 230],
        >>>                   [300,   0, 230, 330, 150],
        >>>                   [250, 230,   0, 240, 120],
        >>>                   [190, 330, 240,   0, 220],
        >>>                   [230, 150, 120, 220,   0]])
        >>> christofides_tsp(graph)
    """
    # 1. escolha um vértice arbitrário como vértice atual.
    currentVertex = source

    # 2. descubra a aresta de menor peso que seja conectada ao vértice atual e a um vértice não visitado V.
    distanceNext = sys.maxsize
    nextVertex = 0
    visitedVertex = []
    lenPath = 0
    arrayDistances = []

    while lenPath < len(matrix[0])-1:
        for i in range(len(matrix[0])):
            if currentVertex != i and i not in visitedVertex:
                if distanceNext > float(matrix[currentVertex][i]):
                    distanceNext = float(matrix[currentVertex][i])
                    nextVertex = i

        # 3. faça o vértice atual ser V.
        V = currentVertex
        currentVertex = nextVertex

        # 4. marque V como visitado.
        visitedVertex.append(V)

        # 5. se todos os vértices no domínio estiverem visitados, encerre o algoritmo.
        if lenPath == len(matrix[0]):

            break
        # 6. Se não vá para o passo 2.
        else:
            lenPath += 1
            arrayDistances.append(distanceNext)
            distanceNext = sys.maxsize

    distanceLastToSource = float(matrix[visitedVertex[0]][nextVertex])
                                  
    arrayDistances.append(distanceLastToSource)
    visitedVertex.append(nextVertex)                             
    visitedVertex.append(visitedVertex[0])

    return [sum(arrayDistances), visitedVertex]

    # print('Menor custo =>', sum(arrayDistances), '\n')
    # print('Melhor caminho =>', visitedVertex)
