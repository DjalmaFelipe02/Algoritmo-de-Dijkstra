import heapq
import os
def dijkstra(grafo, vertice_inicial):
    # Inicialização das distâncias :::: São inicializadas como infinito para todos os vértices, exceto o vértice inicial, que é definido como 0.
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[vertice_inicial] = 0
    anterior = {vertice: "A" for vertice in grafo}
    anterior[vertice_inicial] = "A"

    #Fila de prioridade para armazenar pares (distância, vértice) : Uma fila de prioridade (fila_prioridade) é inicializada com uma tupla contendo a distância e o vértice inicial.
    fila_prioridade = [(0, vertice_inicial)]

    # Algoritmo de Dijkstra 

    while fila_prioridade:
        # Extrai o vértice com a menor distância da fila de prioridade
        # O loop principal continua até que a fila de prioridade não esteja vazia.
        # Em cada iteração, o vértice com a menor distância é extraído, e seus vizinhos são explorados para atualizar as distâncias.
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        # Se encontrarmos um caminho mais curto, ignoramos este vértice
        if distancia_atual > distancias[vertice_atual]:
            continue

        # Explora os vizinhos do vértice atual
        for vizinho, km in grafo[vertice_atual].items():
            # Calcula a nova distância
            nova_distancia = distancia_atual + km

            # Se encontrarmos um caminho mais curto para o vizinho, atualizamos a distância
            # Se for encontrado um caminho mais curto para um vizinho, a distância é atualizada, e o vizinho é adicionado à fila de prioridade com a nova distância.
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anterior[vizinho] = vertice_atual
                # Adiciona o vizinho à fila de prioridade com a nova distância
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return distancias, anterior

#Exemplo de uso com um grafo ponderado direcionado
grafo = {
    'A': {'B': 10, 'C': 5},
    'B': {'A': 10, 'C': 4, 'D': 1, 'E': 4},
    'C': {'A': 5, 'B': 4, 'E': 6},
    'D': {'B': 1, 'E': 2, 'F': 3},
    'E': {'C': 6, 'B': 2, 'D': 4, 'F': 1},
    'F': {'D': 3, 'E': 1},
}

vertice_inicial = 'A'
# Coloca os resultados da função(distancias e anterior) em  duas variáveis.
resultados, resultados2 = dijkstra(grafo, vertice_inicial)
os.system('cls')

print(f"Menores distâncias a partir do vértice {vertice_inicial}:\n")
for vertice, distancia in resultados.items():
    print("A distância de A até "f'{vertice}: {distancia}'" Km passando por ", resultados2[vertice])