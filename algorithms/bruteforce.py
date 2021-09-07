from sys import maxsize
from itertools import permutations

#Travelling Salesman problem solution with brute force
def bruteForce(graph, source):
 
    vertex = []
    for i in range(len(graph)):
        # armazena todos os vértices menos o vértice de origem
        if i != source:
            vertex.append(i)
      
    # armazenar peso mínimo do ciclo hamiltoniano
    min_path = maxsize

    # Armazena o melhor caminho

    next_permutation=permutations(vertex)
    for i in next_permutation:
        # armazenar peso do caminho atual (custo)
        current_pathweight = 0
 
        # calcular o peso do caminho atual
        k = source

        for j in i:
            current_pathweight += float(graph[k][j])
            k = j
        current_pathweight += float(graph[k][source])
        newMinPath = min(min_path, current_pathweight)
        # verificar se o path antigo é maior que o path atual
        if(min_path > newMinPath):
            # atualiza o peso do caminho mínimo
            min_path = min(min_path, current_pathweight)
            pathMin = i
        
    bestPath = []
    for vertices in pathMin:
       bestPath.append(vertices)
    
    #Adicionando o ponto de partida ao inicio da lista e ao final.
    bestPath.insert(0, source)
    bestPath.append(source)


    return [min_path,bestPath]

    # print('Custo minimo =>',min_path)
    # print('Caminho =>', bestPath)
    


