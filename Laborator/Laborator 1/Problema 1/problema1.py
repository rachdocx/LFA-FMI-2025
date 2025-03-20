def load_matrix(matrice):
    try:
        fin = open(matrice, 'r')
    except FileNotFoundError:
        print(f"Eroare: fișierul '{matrice}' nu a fost găsit!")
        return 0

    mat = []
    for line in fin:
        try:
            mat.append([int(x) for x in line.split()])
        except ValueError:
            print(f"Eroare: linia '{line.strip()}' conține caractere invalide!")
            return 0

    fin.close()

    if not mat:
        print("Eroare: fișierul este gol sau nu conține o matrice validă")
        return 0

    n = len(mat[0])
    for line in mat:
        if len(line) != n:
            print("Eroare input-ul nu este o matrice")
            return 0

    return mat


def save_matrix(fn, matrice):
    mat = load_matrix(matrice)
    if mat == 0:
        return

    n = len(mat[0])
    for line in mat:
        if len(line) != n:
            print("Eroare nu este matrice")
            return

    fin = open(fn, 'w')
    for line in mat:
        for x in line:
            fin.write(str(x) + ' ')
        fin.write('\n')
    fin.close()


mat1 = load_matrix('matrice')
print(mat1)
save_matrix('fn', 'matrice')
