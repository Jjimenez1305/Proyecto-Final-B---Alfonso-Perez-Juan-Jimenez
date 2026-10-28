from sys import stdin

def conectar_usuarios():
    #mediante una matriz de adyacencia, por medio de las aristas, representar las conexiones entre usuarios"
    pass

def eliminar_usuarios():
    #modificar la matriz de adyacencia, eliminando las aristas de los usuarios indicados
    pass

def sugerir_personas():
    #hacer una busqueda mediante bfs que permita recomendar las conexiones en común de un usuario con respecto a sus amistades
    pass

def grupos_independientes():
    #identificar las islas que presenta el grafo y retornar los grupos que estas representan
    pass

def contar_amistades():
    #revisar la cantidad de conexiones que tiene un usuario por medio de un recorrido en la matriz de adyacencia
    pass







def main():
    instruccion = stdin.readline()
    while instruccion != "":
        if instruccion == "Conectar usuarios":
            conectar_usuarios()
        elif instruccion == "Eliminar usuarios":
            eliminar_usuarios()
        elif instruccion == "Sugerir personas":
            sugerir_personas()
        elif instruccion == "Grupos independientes":
            grupos_independientes()
        elif instruccion == "Contar amistades":
            contar_amistades()
            



main()
