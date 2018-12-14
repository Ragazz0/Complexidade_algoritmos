from grafos import grafo_dijkstra

def dijkstra(grafo_dijkstra,src,objetivo,visitado=[],distancia={},antecessor={}):
    # Checagem de consistência no grafo
    if src not in grafo_dijkstra:
        raise TypeError('A raiz do menor caminho não foi encontrada!')
    if objetivo not in grafo_dijkstra:
        raise TypeError('O objetivo para traçar o caminho não foi encontrado!')    
    
    if src == objetivo:
        # Definição do menor caminho a ser percorrido
        path=[]
        pred=objetivo
        while pred != None:
            path.append(pred)
            pred=antecessor.get(pred,None)
        print('Menor caminho: '+str(path)+" Custo: "+str(distancia[objetivo])) 
    else :     
        
        # Inicializa caso nó não tenha sido visidado
        if not visitado: 
            distancia[src]=0
        # Visita os nós vizinhos
        for vizinho in grafo_dijkstra[src] :
            if vizinho not in visitado:
                nova_dist = distancia[src] + grafo_dijkstra[src][vizinho]
                if nova_dist < distancia.get(vizinho,float('inf')):
                    distancia[vizinho] = nova_dist
                    antecessor[vizinho] = src
        
        # Marca como visitado
        visitado.append(src)
        
        # 'Seta' os nós não visitados a partir da menor distancia
        nao_visitado={}
        for k in grafo_dijkstra:
            if k not in visitado:
                nao_visitado[k] = distancia.get(k,float('inf'))

        x=min(nao_visitado, key=nao_visitado.get)
        dijkstra(grafo_dijkstra,x,objetivo,visitado,distancia,antecessor)
        
dijkstra(grafo_dijkstra,'s','t')