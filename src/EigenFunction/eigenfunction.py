import numpy.polynomial.polynomial as poly

def detKofaktor(M,row=0,col=0):
    # M adalah sebuah matriks persegi
    # Mengembalikan determinan matriks M (polinom karakteristik matriks M)
    # dengan metode kofaktor rekursif

    # KAMUS LOKAL #


def eigenValue(A):
    # A adalah sebuah matriks persegi
    # Mengembalikan nilai-nilai eigen melalui akar-akar
    # persamaan karakteristik dari A dengan metode kofaktor

    # KAMUS LOKAL
    # EigMat : polynomial[][]
    # charPol : polynomial
    # i : int

    # ALGORITMA
    EigMat = [X for X in A]  # buat matriks A - λI
    for i in range(0,len(EigMat)):  # Karena EigMat adalah matriks persegi, jumlah baris dan kolom sama
        EigMat[i][i] = (EigMat[i][i], -1)
    
    charPol = detKofaktor(EigMat)
    return poly.polyroots(charPol)