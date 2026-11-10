from sys import stdin

def registrar_usuario(nodos: list, usuario: str):
    nodos.append(usuario)
    return nodos

def conectar_usuarios(u1: str, u2: str, grafo):
    grafo[u1].add(u2)
    return grafo

def remover_usuario(u_rem:str,grafo:dict):
    for usuario in grafo:
        grafo[usuario].discard(u_rem)
    return grafo

def eliminar_usuarios(u: str, grafo: dict):
    remover_usuario(u,grafo)
    grafo.pop(u)
    return grafo

def sugerir_personas(u_sg:str, grafo: dict):
    recomendados = []
    for i in grafo:
        for j in grafo[i]:
            if j == u_sg:
                recomendados.append(i)
    return recomendados

def grupos_independientes():
    pass

def contar_seguidores(uc: str, grafo: dict):
    seguidores = 0
    for usuario in grafo[uc]:
        if uc in grafo[usuario]:
            seguidores += 1

    return f"{uc} tiene {seguidores} seguidores"
            


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
            usuario_1 = instruccion[1]
            usuario_2 = instruccion[2]
            if usuario_1 in nodos and usuario_2 in nodos:
                if usuario_2 not in grafo[usuario_1]:
                    grafo = conectar_usuarios(usuario_1, usuario_2, grafo)
        elif instruccion[0] == 'Remover':
            usuario_remover = instruccion[1]
            grafo = remover_usuario(usuario_remover,grafo)
            print(f'R{grafo}')
        elif instruccion[0] == "Eliminar":
            usuario_sg = instruccion[1]
            grafo = eliminar_usuarios(usuario, grafo)
            print(f'E{grafo}')
        elif instruccion[0] == "Sugerir":
            usuario_sg = instruccion[1]
            sugeridos = sugerir_personas(usuario_sg, grafo)
            for usuario_sug in sugeridos:
                print(f"Sugerencias para {usuario_sg} : {usuario_sug}")
        elif instruccion[0] == "Grupos":
            grupos_independientes()
        elif instruccion[0] == "Contar":
            usuario_cont = instruccion[1]
            print(contar_seguidores(usuario_cont, grafo))
        else:
            print("Instrucción invalida")

        instruccion = [str(i) for i in stdin.readline().strip().split()]
    print(grafo)
main()
