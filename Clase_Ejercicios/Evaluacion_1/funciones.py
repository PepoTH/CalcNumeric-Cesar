import numpy as np

def sistemas(valor,desde,hacia):
    if(desde=='Bin'):
        return binario(valor,hacia)
    elif(desde=='Dec'):
        return decimal(valor,hacia)
    elif(desde == 'Hex'):
        return hexa(valor,hacia)
    elif(desde=='Oct'):
        return octa(valor,hacia)
    elif(desde=='Ter'):
        return basen(valor,hacia,3)
    elif(desde=='Cuar'):
        return basen(valor,hacia,4)
    
def binario(valor,hacia):
    try:
        if(hacia=='Dec'):
            return int(valor,2)
        elif(hacia == 'Hex'):
            return str(hex(int(valor)))[2:].upper()
        elif(hacia == 'Oct'):
            return str(oct(int(valor)))[2:]
        elif(hacia == 'Ter'):
            return toBase(binario(valor,'Dec'),3)
        elif(hacia == 'Cuar'):
            return toBase(binario(valor,'Dec'),4)
        else:
            return valor
    except ValueError:
        return 'Error'

def decimal(valor,hacia):
    try:
        if(hacia=='Bin'):
            return bin(int(valor))[2:]
        elif(hacia == 'Hex'):
            return str(hex(int(valor)))[2:].upper()
        elif(hacia == 'Oct'):
            return str(oct(int(valor)))[2:]
        elif(hacia == 'Ter'):
            return toBase(valor,3)
        elif(hacia == 'Cuar'):
            return toBase(valor,4)
        else:
            return valor
    except ValueError:
        return 'Error'
    
def hexa(valor,hacia):
    try:
        if(hacia=='Bin'):
            return bin(int(valor))[2:]
        elif(hacia == 'Dec'):
            return int(valor,16)
        elif(hacia == 'Oct'):
            return str(oct(int(valor)))[2:]
        elif(hacia == 'Ter'):
            return toBase(hexa(valor,'Dec'),3)
        elif(hacia == 'Cuar'):
            return toBase(hexa(valor,'Dec'),4)
        else:
            return valor
    except ValueError:
        return 'Error'
    
def octa(valor,hacia):
    try:
        if(hacia=='Bin'):
            return bin(int(valor))[2:]
        elif(hacia == 'Dec'):
            return int(valor,8)
        elif(hacia == 'Hex'):
            return oct(int(valor))
        elif(hacia == 'Ter'):
            return toBase(octa(valor,'Dec'),3)
        elif(hacia == 'Cuar'):
            return toBase(octa(valor,'Dec'),4)
        else:
            return valor
    except ValueError:
        return 'Error'
    
def basen(valor,hacia,n):
    try:
        valor = str(int(valor,n))
        if(hacia=='Dec'):
            return valor
        elif(hacia=='Bin'):
            return decimal(valor,hacia)
        elif(hacia=='Hex'):
            return decimal(valor,hacia)
        elif(hacia=='Oct'):
            return decimal(valor,hacia)
        elif(hacia == 'Ter'):
            return toBase(int(valor),3)
        elif(hacia == 'Cuar'):
            return toBase(int(valor),4)
    except ValueError:
        return 'Error'
    
def toBase(valor,base):
    word = ''
    valor = int(valor)
    while valor:
        word += str(valor % base)
        valor //= base
    return word[::-1]

def seidel(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.copy(x0)
    for it in range(max_iter):
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(i) if j != n)
            s += sum(A[i, j] * x[j] for j in range(i + 1, n))
            s += b[i]
            x[i] = s / A[i, i]
        if np.linalg.norm(x - x0) < tol:
            return x
        x0 = np.copy(x)
    
