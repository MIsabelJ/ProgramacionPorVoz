import services.assign.assignBranch as assignBranch
import services.create.createBranch as createBranch


def abrirNodo(palabraDividida, arrayIdentificadores):
    for palabra in palabraDividida:
        if palabra == "crear":
            palabraDividida.remove("crear")
            createBranch.crear(palabraDividida, arrayIdentificadores)
            break
        if palabra == "llamar":
            palabraDividida.remove("llamar")
            break
        if palabra == "eliminar":
            palabraDividida.remove("eliminar")
            break
        if palabra == "asignar":
            palabraDividida.remove("asignar")
            assignBranch.asignar(palabraDividida, arrayIdentificadores)
            break
        if palabra == "comentar":
            palabraDividida.remove("comentar")
            break
        if palabra == "mover":
            palabraDividida.remove("mover")
            break
        if palabra == "insertar":
            palabraDividida.remove("insertar")
            break
