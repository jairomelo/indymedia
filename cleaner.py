import os

def crear_clear_list():
    filetext = open("clear_list_raw.txt", "r", encoding="utf-8")

    # delete all endlines
    filetexto = filetext.read().replace('\n', ' ')

    lista_palabras = filetexto.split()

    lista_palabras_unicas = []

    for lp in lista_palabras:
        if lp not in lista_palabras_unicas:
            lp = lp.lower().replace(".", "").replace(",", "").replace("\'", "")
            lista_palabras_unicas.append(lp)

    # write list to file
    filetextoclean = open("clear_list.txt", "w", encoding="utf-8")
    filetextoclean.write(str(lista_palabras_unicas))
    filetextoclean.close()


def listado_palabras_vacias():
    # import text as list

    listado_palabras_vacias = open("clear_list.txt", "r", encoding="utf-8")
    lpv = listado_palabras_vacias.read().split()
    lpv = [lp.replace("\'", "") for lp in lpv]
    # replace punctuation
    lpv = [lp.replace(".", "").replace("]", "").replace("[", "") for lp in lpv]
    lpv  = [lp.strip('.,:;!¡?¿') for lp in lpv]
    return lpv

if __name__ == "__main__":
    if not os.path.exists("clear_list.txt"):
        crear_clear_list()
    print(listado_palabras_vacias())