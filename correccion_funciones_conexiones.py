from sys import stdin

def registrar_usuario(nodos: list, usuario: str):
    nodos.append(usuario)
    return nodos

def conectar_usuarios(u1: str, u2: str, grafo):
    grafo[u1].add(u2)
    return grafo

def eliminar_usuarios(u:str,grafo):
    grafo.pop(u)
    return grafo

def sugerir_personas(u_sg:str,grafo):
    recomendados = []
    for i in grafo:
        for j in grafo[i]:
            if j == u_sg:
                recomendados.append(i)
    return recomendados
            

def grupos_independientes():
    pass

def contar_amistades():
    pass







def main():
    instruccion = [str(i) for i in stdin.readline().strip().split()]
    nodos = []
    grafo = {}
    while instruccion != []:
        if instruccion[0] == "Registrar":
            usuario = instruccion[1]
            if usuario not in nodos:
                    nodos = registrar_usuario(nodos, usuario)
                    grafo[usuario] = set()
        elif instruccion[0] == "Conectar":
            usuario_1 = str(stdin.readline().strip())
            usuario_2 = str(stdin.readline().strip())
            if usuario_1 in nodos and usuario_2 in nodos:
                if usuario_2 not in grafo[usuario_1]:
                    grafo = conectar_usuarios(usuario_1, usuario_2, grafo)
        elif instruccion[0] == "Eliminar":
            usuario = str(stdin.readline().strip())
            grafo = eliminar_usuarios(usuario,grafo)
        elif instruccion[0] == "Sugerir":
            usuario_sg = str(stdin.readline().strip())
            sugeridos = sugerir_personas(usuario_sg,grafo)
            print(sugeridos)
        elif instruccion[0] == "Grupos":
            grupos_independientes()
        elif instruccion[0] == "Contar":
            contar_amistades()
        else:
            print("Instrucción invalida")

        instruccion = [str(i) for i in stdin.readline().strip().split()]
    print(grafo)
main()
