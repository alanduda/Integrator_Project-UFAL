from utils.readFile import readFile
from sys import maxsize
V = 4

# implementation of traveling Salesman Problem


def travellingSalesmanProblem(graph, source):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(len(graph)):
        if i != source:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize

    while True:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = source
        for i in range(len(vertex)):
            current_pathweight += float(graph[k][vertex[i]])
            k = vertex[i]
        current_pathweight += float(graph[k][source])

        # update minimum
        min_path = min(min_path, current_pathweight)

        if not next_permutation(vertex):
            break

    return min_path

# next_permutation implementation


def next_permutation(L):

    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True


# Driver Code
if __name__ == "__main__":

    # matrix representation of graph
    graph = readFile('inputs/sh07_dist.txt')
    source = 0
    print('custo minimo:', travellingSalesmanProblem(graph, source))
