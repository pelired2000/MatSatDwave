# Comprobar su una expresión CNF es satisfactible

# Lectura del contenido del fichero dimacs de entrada
def leer_fich_cnf(ficherocnf):
    with open(ficherocnf) as ficherocnf:
        return ficherocnf.readlines()

# Inicialización del número de variables: Num_Vars
num_vars = 0
num_clas = 0
lista_clausulas = []


# Obtención de las cláusulas del fichero DIMACS
def parse_fich_cnf(ficherocnf):
    global num_vars
    global num_clas
    global lista_clausulas

    clausulas_fichero = leer_fich_cnf('clausulas.cnf')
    print(clausulas_fichero)

    cnf = list()
    linea_cnf = list()

    for linea in clausulas_fichero:
        literales = linea.split()
        # print(literales)
        if len(literales) != 0:
            if literales[0] not in ("p", "c"):
                for literal in literales:
                    # print(literal)
                    lit = int(literal)
                    if lit == 0:
                        cnf.append(sorted(linea_cnf, key=abs))
                        linea_cnf = list()
                    else:
                        linea_cnf.append(lit)

            else:
                if literales[0] == "p":
                    num_vars = int(literales[2])
                    num_clas = int(literales[3])
    # print(cnf)
    lista_clausulas = cnf

# Generar cadena con la combinación de entrada binaria de N bits a partir de su valor decimal
def gen_comb_entrada(val_dec,num_vars):
    combbin = [int(i) for i in list('{0:0b}'.format(val_dec).zfill(num_vars))]
    return combbin

# Comprobamos la satisfabilidad de las clausulas
def satisfastible(ficherocnf):

    parse_fich_cnf(ficherocnf)

    print(f'-Num Variables: {num_vars}')
    print(f'-Num Clausulas: {num_clas}')
    print(f'-Lista de clausulas ordenadas: {lista_clausulas}')
    #print(f'Combinaciones de entrada:{comb_entrada}')
    nsat = 3
    ind_cl = 0
    ind_entr = 0
    sat_cla = 0
    num_sat = 0
    num_combs_entrada = (2 ** num_vars) - 1
    print(f'Nº de entradas posibles: {num_combs_entrada}')

    while ind_entr <= num_combs_entrada and num_sat < num_clas:
        clausula = lista_clausulas[ind_cl]
        print(f'Clausula:{clausula}')
        #entrada = comb_entrada[ind_entr]
        entrada = gen_comb_entrada(int(ind_entr), num_vars)
        print(f'Entrada:{entrada}')
        ind_lits = 0
        sat_cla = 0
        while ind_lits < nsat and sat_cla == 0:
            if (clausula[ind_lits] > 0 and entrada[abs(clausula[ind_lits])-1] == 1) or (
                    clausula[ind_lits] < 0 and entrada[abs(clausula[ind_lits])-1] == 0):
                sat_cla = 1
                num_sat += 1
                ind_cl += 1
            else:
                ind_lits += 1

        if sat_cla == 0:
            ind_entr += 1
            ind_cl = 0
            num_sat = 0

    if num_sat == num_clas:
        # return 1
        print(f'Entrada que satisface la expresión CNF:{entrada}')
        print('1')
    else:
        # return 0
        print('0')

# Lectura del fichero dimacs
# print('Lectura fichero DIMACS')
# fichero_cnf = leer_fich_cnf('clausulas.cnf')
# print(f'Fichero CNF: {fichero_cnf}')
#
# # Obtención de la información del fichero dimacs
# print('Parseado del fichero DIMACS')
# parse_fich_cnf('clausulas.cnf')
# print('Datos del fichero CNF:')
#
# print(f'-Num Variables: {num_vars}')
# print(f'-Num Clausulas: {num_clas}')
# print(f'-Lista de clausulas: {lista_clausulas}')

satisfastible('clausulas.cnf')
