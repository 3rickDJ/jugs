import collections

def main():

    nodo_inicial = [[0, 0]]
    jarras = [3,4]
    objetivo = 2
    visitados = {}
    busqueda(nodo_inicial, jarras, objetivo, visitados)

def obtenerIndice(node):
    # la llave unica de un estado para ponerla en el diccinario y que no colisiones
    return pow(7, node[0]) * pow(5, node[1])

def esObjetivo(camino, objetivo):
    return camino[-1][1] == objetivo

def esRevisado(node, visitado):
    # revisar si ya añadimos ese nodo a la frontera
    # si fue visitado returnar el valor del nodo, True, de otra forma False
    return visitado.get(obtenerIndice(node), False)

def siguientes(jarras, camino, visitado):
    resultado = []
    siguientes_nodos = []
    nodo = []

    primera_jarra_max = jarras[0]
    segunda_jarra_max = jarras[1]

    a = camino[-1][0]  # cantidad inicial de la primera jarra
    b = camino[-1][1]  # cantidad inicial de la segunda jarra

    # 1. llena la primera jarra
    nodo.append(primera_jarra_max)
    nodo.append(b)
    if not esRevisado(nodo, visitado):
        siguientes_nodos.append(nodo)
    nodo = []

    # 2. llena la segunda jarra
    nodo.append(a)
    nodo.append(segunda_jarra_max)
    if not esRevisado(nodo, visitado):
        siguientes_nodos.append(nodo)
    nodo = []

    # 3. vertir la segunda jarra dentro de la primera
    nodo.append(min(primera_jarra_max, a + b))
    nodo.append(b - (nodo[0] - a))  # b - ( a' - a)
    if not esRevisado(nodo, visitado):
        siguientes_nodos.append(nodo)
    nodo = []

    # 4. vertir la primera jarra dentro de la segunda
    nodo.append(min(a + b, segunda_jarra_max))
    nodo.insert(0, a - (nodo[0] - b))
    if not esRevisado(nodo, visitado):
        siguientes_nodos.append(nodo)
    nodo = []

    # 5. primera jarra vacía
    nodo.append(0)
    nodo.append(b)
    if not esRevisado(nodo, visitado):
        siguientes_nodos.append(nodo)
    nodo = []

    # 6. segunda jarra vacía
    nodo.append(a)
    nodo.append(0)
    if not esRevisado(nodo, visitado):
        siguientes_nodos.append(nodo)

    # lista de los siguiente nodos
    for i in range(0, len(siguientes_nodos)):
        temp = list(camino)
        temp.append(siguientes_nodos[i])
        resultado.append(temp)

    if len(siguientes_nodos) == 0:
        #ya no hay mas nodos por generar
        # ya sea por que no son validos o ya han sido visitados
        pass
    else:
        # print("Movimientos válidos")
        print(siguientes_nodos)
    return resultado

def busqueda(nodo_inicial, jarras, cantidad_objetivo, visitado):
    objetivo = []
    completado = False

    cola = collections.deque()
    cola.appendleft(nodo_inicial)

    while len(cola) != 0:
        path = cola.popleft()
        print(path)
        visitado[obtenerIndice(path[-1])] = True
        if esObjetivo(path, cantidad_objetivo):
            completado = True
            objetivo = path
            break

        siguientes_movimientos = siguientes(jarras, path, visitado)
        for i in siguientes_movimientos:
            cola.append(i)

    if completado:
        print("Solución 🔥😍🥑👌🏼")
        print(objetivo)
    else:
        print("No se encontró una solución 😭")


if __name__ == '__main__':
    main()
