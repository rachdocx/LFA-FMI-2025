def save_matrix(fn,matrice):
    fin=open(fn,'w')
    mat=load_matrix(matrice)
    if mat==0:
        return
    n=len(mat[0])
    for line in mat:
        if len(line)!=n:
            print("Eroare nu este matrice")
            return
    for line in mat:
        for x in line:
            fin.write(str(x)+' ')
        fin.write('\n')

def load_matrix(matrice):
    fin=open(matrice,'r')
    mat=[[int(x) for x in line.split()] for line in fin.readlines()]
    n=len(mat[0])
    for line in mat:
        if len(line)!=n:
            print("Eroare input-ul nu este o matrice")
            return 0
    return mat

mat1=[]
mat1=load_matrix('matrice')
print (mat1)
save_matrix('fn','matrice')
