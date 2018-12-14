from grafos import grafo

# Busca
def bfs_search(grafo, atual):
    visitado, fila = set(), [atual]
    while fila:
        vertice = fila.pop(0)
        if vertice not in visitado:
            visitado.add(vertice)
            fila.extend(grafo[vertice] - visitado)
    return visitado

# Possíveis caminhos
def bfs_paths(grafo, atual, busca):
    fila = [(atual, [atual])]
    while fila:
        (vertice, path) = fila.pop(0)
        for next in grafo[vertice] - set(path):
            if next == busca:
                yield path + [next]
            else:
                fila.append((next, path + [next]))

resultado = bfs_search(grafo, 'A')
caminhos = list(bfs_paths(grafo, 'A', 'B'))

print('Grafo: ', grafo)
print('Resultado da busca: ', resultado)
print('Possíveis caminhos: ', caminhos)