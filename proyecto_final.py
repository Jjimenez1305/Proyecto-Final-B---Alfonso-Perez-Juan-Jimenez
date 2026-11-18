from sys import stdin

def verificar_usuario(grafo:dict,usuario:str):
    if usuario not in grafo:
        return True
    else:
        return False

def registrar_usuario(grafo: dict, usuario: str):
    grafo[usuario] = set()
    return grafo

def conectar_usuarios(u1: str, u2: str, grafo):
    grafo[u1].add(u2)
    return grafo

def desconectar_usuario(u_rem:str, grafo:dict):
    if u_rem in grafo: 
        for usuario in grafo:
            if u_rem in grafo[usuario]:
                grafo[usuario].remove(u_rem)
    return grafo

def eliminar_usuarios(u: str, grafo: dict):
    if u in grafo:
        desconectar_usuario(u,grafo)
        grafo.pop(u)
    return grafo

def sugerir_personas(u_sg:str, grafo: dict):
    recomendados = []
    for i in grafo:
        for j in grafo[i]:
            if j == u_sg:
                recomendados.append(i)
    return recomendados

def grupos_independientes(grafo: dict):
    visitados = set()
    islas = 0

    vecinos = {u: set() for u in grafo}

    for u in grafo:
        for v in grafo[u]:
            vecinos[u].add(v)
            vecinos[v].add(u)

    def dfs(u):
        visitados.add(u)

        for vecino in vecinos[u]:
            if vecino not in visitados:
                dfs(vecino)

    for vertice in grafo:
        if vertice not in visitados:
            islas += 1
            dfs(vertice)
            
    return islas

def contar_seguidores(uc: str, grafo: dict):
    seguidores = 0
    for usuario in grafo:
        if uc in grafo[usuario] :
            seguidores += 1

    return f"{uc} tiene {seguidores} seguidores"
            


def main():
    instruccion = [str(i) for i in stdin.readline().strip().split()]
    grafo = {}
    
    while instruccion != []:
        if instruccion[0] == "Registrar":
            usuario = instruccion[1]
            verificacion = verificar_usuario(grafo,usuario)
            if verificacion:
                grafo = registrar_usuario(grafo, usuario)
                    
        elif instruccion[0] == "Conectar":
            usuario_1 = instruccion[1]
            usuario_2 = instruccion[2]
            verificacion_u1 = verificar_usuario(grafo,usuario_1)
            verificacion_u2 = verificar_usuario(grafo,usuario_2)
            if not verificacion_u1 and not verificacion_u2:
                if usuario_2 not in grafo[usuario_1]:
                    grafo = conectar_usuarios(usuario_1, usuario_2, grafo)
                    
        elif instruccion[0] == 'Desconectar':
            usuario_desconectar = instruccion[1]
            verificacion = verificar_usuario(grafo,usuario_desconectar)
            if not verificacion:
                grafo = desconectar_usuario(usuario_desconectar,grafo)
            else:
                print(f'No se puede desconectar el usuario {usuario_desconectar} porque no existe en la red.')
            
        elif instruccion[0] == "Eliminar":
            usuario_eliminar = instruccion[1]
            if usuario_sg in grafo:
                grafo = eliminar_usuarios(usuario_sg, grafo)
            else:
                print(f'No se puede eliminar el usuario {usuario_eliminar} porque no existe en la red.')

        elif instruccion[0] == "Sugerir":
            usuario_sg = instruccion[1]
            verificacion_sg = verificar_usuario(grafo,usuario_sg)
            if not verificacion_sg:
                sugeridos = sugerir_personas(usuario_sg, grafo)
                for usuario_usg in sugeridos:
                    if sugeridos != []:
                        print(f"Sugerencias para {usuario_sg} : {usuario_usg}")
                    else:
                        print(f"No hay sugerencias para {usuario_sg}")
        elif instruccion[0] == "Grupos":
            print(grupos_independientes(grafo))
            
        elif instruccion[0] == "Contar":
            usuario_cont = instruccion[1]
            verificacion_ucont = verificar_usuario(grafo,usuario_cont)
            if not verificacion_ucont:
                print(contar_seguidores(usuario_cont, grafo))
            
        else:
            print("Instrucción invalida")

        instruccion = [str(i) for i in stdin.readline().strip().split()]

main()
