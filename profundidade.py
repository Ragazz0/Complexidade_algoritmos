from grafos import grafo

# Busca
def dfs_search(grafo, atual, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(atual)
    for next in grafo[atual] - visitado:
        dfs_search(grafo, next, visitado)
    return visitado

# Possíveis caminhos
def dfs_paths(grafo, atual, objetivo):
    stack = [(atual, [atual])]
    while stack:
        (vertice, path) = stack.pop()
        for next in grafo[vertice] - set(path):
            if next == objetivo:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

resultado = dfs_search(grafo, 'C')
caminhos = list(dfs_paths(grafo, 'A', 'F'))

print('Grafo: ', grafo)
print('Resultado da busca: ', resultado)
print('Possíveis caminhos: ', caminhos)