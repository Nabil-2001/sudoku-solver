def nbVide(T):
    counter = 0
    for i in range(9):
        for j in range(9):
            if T[i][j] == 0:
                counter += 1
    return counter

def f(i,j):
    return (9*i + j)

def carre(T,i,j):
    if 0 <= i <= 2:
        if 0 <= j <= 2:
            return 1
        elif 3 <= j <= 5:
            return 2
        else:
            return 3
    elif 3 <= i <= 5:
        if 0 <= j <= 2:
            return 4
        elif 3 <= j <= 5:
            return 5
        else:
            return 6
    elif 6 <= i <= 8:
        if 0 <= j <= 2:
            return 7
        elif 3 <= j <= 5:
            return 8
        else:
            return 9

def verifL(T,i,x):
    for j in range(9):
        if T[i][j] == x:
            return True
    return False

def verifC(T,j,x):
    for i in range(9):
        if T[i][j] == x:
            return True
    return False

def verifR(T,i,j,x):
    for k in range(9):
        for p in range(9):
            if carre(T,k,p) == carre(T,i,j):
                if T[k][p] == x:
                    return True
    return False

def estPossible(T,i,j,x):
    if verifR(T,i,j,x) == False and verifL(T,i,x) == False and verifC(T,j,x) == False:
        return True
    return False

def init(P):
    for i in range(81):
        for j in range(9):
            P[i][j] = 0

def remplirP(T,P):
    for i in range(9):
        for j in range(9):
            if T[i][j] == 0:
                for x in range(1,10):
                    if estPossible(T,i,j,x) == True:
                        P[f(i,j)][x-1] = 1

def val(P,T,i,j):
    counter = 0
    for k in range(9):
        if P[f(i,j)][k] == 1:
            counter += 1
            val = k+1
    if counter == 1:
        return val
    else:
        return 0

def remplirT(T,P):
    counter = nbVide(T)
    while counter > 0:
        remplirP(T,P)
        for i in range(9):
            for j in range(9):
                if T[i][j] == 0:
                    T[i][j] = val(P,T,i,j)
        counter = nbVide(T)
    return T

def LancerJeu(T):
    print(T)
    P = [[0]*9 for i in range(81)]
    Tsol = remplirT(T,P)
    print(Tsol)

T = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
LancerJeu(T)
