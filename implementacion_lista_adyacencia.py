from sys import stdin

def registrar_usuario(nodos: list, usuario: str):
    nodos.append(usuario)
    return nodos

def conectar_usuarios():
    pass

def eliminar_usuarios():
    pass

def sugerir_personas():
    pass

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
            nodos = registrar_usuario(nodos, usuario)
            grafo[usuario] = {}
        elif instruccion[0] == "Conectar":
            conectar_usuarios()
        elif instruccion[0] == "Eliminar":
            eliminar_usuarios()
        elif instruccion[0] == "Sugerir":
            sugerir_personas()
        elif instruccion[0] == "Grupos":
            grupos_independientes()
        elif instruccion[0] == "Contar":
            contar_amistades()
        else:
            print("Instrucción invalida")

        instruccion = [str(i) for i in stdin.readline().strip().split()]

    print(nodos)

main()
