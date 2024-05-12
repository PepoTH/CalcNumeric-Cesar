def sistemas(valor,desde,hacia):
    if(desde=='Bin'):
        return binario(valor,hacia)
    elif(desde=='Dec'):
        return decimal(valor,hacia)
    elif(desde == 'Hex'):
        return hexa(valor,hacia)
    elif(desde=='Oct'):
        return octa(valor,hacia)
    
def binario(valor,hacia):
    try:
        if(hacia=='Dec'):
            return int(valor,2)
        elif(hacia == 'Hex'):
            return str(hex(int(valor)))[2:].upper()
        elif(hacia == 'Oct'):
            return str(oct(int(valor)))[2:]
        else:
            return valor
    except ValueError:
        return 'Error'

def decimal(valor,hacia):
    try:
        if(hacia=='Bin'):
            return bin(int(valor,2))[2:]
        elif(hacia == 'Hex'):
            return str(hex(int(valor)))[2:].upper()
        elif(hacia == 'Oct'):
            return str(oct(int(valor)))[2:]
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
        else:
            return valor
    except ValueError:
        return 'Error'