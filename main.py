from sys import stdin

<<<<<<< HEAD
def registrar_usuario(nodos:list,usuario:str):
    nodos.append(usuario)
    return nodos
   

def construir_grafo(grafo: list):
    for fila in grafo:
        fila.append(0)                    
    grafo.append([0] * (len(grafo) + 1))  
    return grafo

def conectar_usuarios(i: int, j: int, grafo: list):
    grafo[i][j] = 1
    grafo[j][i] = 1                     
    return grafo



def eliminar_usuarios(usuario_1:str,usuario_2:str):
    #modificar la matriz de adyacencia, eliminando las aristas de los usuarios indicados
    matriz[usuario_1][usuario_2] = 0
    matriz[usuario_2][usuario_1] = 0
    return matriz
=======
def conectar_usuarios():
    #mediante una matriz de adyacencia, por medio de las aristas, representar las conexiones entre usuarios"
    pass

def eliminar_usuarios():
    #modificar la matriz de adyacencia, eliminando las aristas de los usuarios indicados
    pass
>>>>>>> eb5325815f89cf0fcd86be01b3252718b46cfe59

def sugerir_personas():
    #hacer una busqueda mediante bfs que permita recomendar las conexiones en común de un usuario con respecto a sus amistades
    pass

def grupos_independientes():
    #identificar las islas que presenta el grafo y retornar los grupos que estas representan
    pass

def contar_amistades():
    #revisar la cantidad de conexiones que tiene un usuario por medio de un recorrido en la matriz de adyacencia
    pass

<<<<<<< HEAD
def imprimir_grafo(grafo):
    for i in range(len(grafo)):
        print(f"Usuario [{i}] conectado con: {grafo[i]}")


def main():
    instruccion = stdin.readline().strip()
    nodos = []
    indices = {}
    grafo = []                            

    instruccion = stdin.readline().strip()
    while instruccion != "":
        if instruccion == "Registrar usuario":
            usuario = stdin.readline().strip()
            if usuario != "" and usuario not in indices:
                indices[usuario] = len(nodos)
                nodos = registrar_usuario(nodos, usuario)
                print(nodos)
                grafo = construir_grafo(nodos)
                imprimir_grafo(grafo)
        elif instruccion == "Conectar usuarios":
            usuario_1 = stdin.readline().strip()
            usuario_2 = stdin.readline().strip()
            if usuario_1 in indices and usuario_2 in indices and usuario_1 != usuario_2:
                grafo = conectar_usuarios(indices[usuario_1], indices[usuario_2], grafo)
                imprimir_grafo(grafo)
            else:
                print("Usuario no válido")
=======






def main():
    instruccion = stdin.readline()
    while instruccion != "":
        if instruccion == "Conectar usuarios":
            conectar_usuarios()
>>>>>>> eb5325815f89cf0fcd86be01b3252718b46cfe59
        elif instruccion == "Eliminar usuarios":
            eliminar_usuarios()
        elif instruccion == "Sugerir personas":
            sugerir_personas()
        elif instruccion == "Grupos independientes":
            grupos_independientes()
        elif instruccion == "Contar amistades":
            contar_amistades()
<<<<<<< HEAD
        instruccion = stdin.readline().strip()
=======
            
>>>>>>> eb5325815f89cf0fcd86be01b3252718b46cfe59



main()
