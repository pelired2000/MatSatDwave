# Generación de ficheros de prueba:  num_vars: 3..10 y num_clausulas: 1..10

import os
import random

num_vars = 3
num_claus = 10
n_agrup = 3

def crear_clausulas(n_vars, n_claus, n_agr):

    lista_clausulas = []
    str_lista_cl = ""
    num_cl = 0
    valores = range(1, n_vars + 1)
    limite_cla = 2 ** int(n_vars)

    while num_cl < min(n_claus,limite_cla) :
        lista_valores = sorted(random.sample(valores, n_agr))
        # print(lista_valores)

        lista_signos = random.choices([-1,1], k = len(lista_valores))
        # print(lista_signos)

        producto = [a * b for a, b in zip(lista_valores, lista_signos)]
        # print(producto)

        if  producto not in lista_clausulas:
            lista_clausulas.append(producto)
            # print(f'Añadido {producto} a la lista de clausulas :)')
            str_lista_cl = str_lista_cl + ' '.join(str(x) for x in producto) + " 0\n"
            num_cl += 1

    return(str_lista_cl)

# lista_clausulas_gen = crear_clausulas(num_vars, num_claus, n_agrup)
# print(lista_clausulas_gen)


def genfichpbas():

    for i in range(3, 11):
        carp_i = format("nvar" + str(i)).zfill(4)
        limite_cla = 2 ** int(i)
        for j in range(1, min(11,limite_cla+1)):
            carp_j = format("ncla" + str(j)).zfill(4)
            for k in range(1, 6):
                ruta_fich = os.getcwd() + "\\fichspba\\" + carp_i + "\\" + carp_j + "\\"
                nomb_fich = "pba" + format(str(i)).zfill(4) + format(str(j)).zfill(4) + str(k) + ".cnf"

                try:
                    if not os.path.exists(ruta_fich):
                        os.makedirs(ruta_fich)

                    with open(os.path.join(ruta_fich, nomb_fich), 'w') as fp:
                        fp.write(f'c Fichero de Prueba {nomb_fich}' + "\n")
                        fp.write(f"p cnf {i} {min(j,limite_cla)}" + "\n")
                        fp.write(crear_clausulas(i, j, n_agrup))

                        print(f'El fichero {nomb_fich} se creó correctamente :)!!')

                except:
                    print(f'Error!! El fichero {ruta_fich} no pudo crearse :(!!')

genfichpbas()