def sistemas(valor,opcion):
    if(opcion == 'Dec'):
        return int(valor,2)
    elif(opcion == 'Bin'):
        print(esBin(int(valor)))
    
def esBin(n):

    try:
        bin(n)
        return True
    except ValueError or OverflowError:
        return False