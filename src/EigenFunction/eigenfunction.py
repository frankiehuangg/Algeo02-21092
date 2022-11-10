import numpy.polynomial.polynomial as poly

def polyKofaktor(M):
    # M adalah sebuah matriks persegi
    # Mengembalikan determinan matriks M (polinom karakteristik matriks M)
    # dengan metode kofaktor rekursif

    # KAMUS LOKAL
    # minorMat : polynomial[][]
    # polyEq, polyTmp : polynomial
    # dim : int
    # i, j, k = int

    # ALGORITMA
    dim = len(M)
    if(dim == 1):
        return M[0][0]
    else:
        minorMat = [[0 for i in range(dim-1)] for i in range(dim-1)]
        polyEq = 0
        for i in range(dim):
            # Copy matriks minor
            for j in range(1, dim):
                for k in range(i):
                    minorMat[j-1][k] = M[j][k]

            for j in range(1, dim):
                for k in range(i+1, dim):
                    minorMat[j-1][k-1] = M[j][k]

            # hitung polynomial
            polyTmp = poly.polymul(M[0][i], polyKofaktor(minorMat))
            if(i%2 == 0):
                polyTmp = [(-x) for x in polyTmp]
            polyEq = poly.polyadd(polyEq, polyTmp)

        return polyEq


def eigenValue(A):
    # A adalah sebuah matriks persegi
    # Mengembalikan nilai-nilai eigen melalui akar-akar
    # persamaan karakteristik dari A dengan metode kofaktor

    # KAMUS LOKAL
    # eigMat : polynomial[][]
    # charPol : polynomial
    # i : int

    # ALGORITMA
    eigMat = [X for X in A]  # buat matriks A - λI
    for i in range(0,len(eigMat)):  # Karena eigMat adalah matriks persegi, jumlah baris dan kolom sama
        eigMat[i][i] = (eigMat[i][i], -1)
    
    charPol = polyKofaktor(eigMat)
    return poly.polyroots(charPol)