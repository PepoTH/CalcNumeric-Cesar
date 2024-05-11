


def binario(txt = '',opcion = ''):
    try:
        if(txt.isnumeric()):
            if(opcion == 'D'):
                return int(txt,2)
            elif(opcion == 'H'):
                return int(txt,16)
            elif(opcion == 'O'):
                return int(txt,8)
    except ValueError:
        return 'Numero Incorrecto'

        
def decimal(txt = '',opcion = ''):
    if(txt.isnumeric()):
        if(opcion == 'B'):
            return int(txt,0b)
        elif(opcion == 'H'):
            return int(txt,16)
        elif(opcion == 'O'):
            return int(txt,8)
        
def octal(txt = '',opcion = ''):
    if(txt.isnumeric()):
        if(opcion == 'B'):
            return int(txt,2)
        elif(opcion == 'H'):
            return int(txt,16)
        elif(opcion == 'D'):
            return int(txt,10)
        
def hexa(txt = '',opcion = ''):
    if(txt.isnumeric()):
        if(opcion == 'B'):
            return int(txt,2)
        elif(opcion == 'D'):
            return int(txt,10)
        elif(opcion == 'O'):
            return int(txt,8)

#De binario a cualquiera
        
valor = '36'
opcion = 'D'

print(decimal(valor,'B'))