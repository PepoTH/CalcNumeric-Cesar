import flet as ft

class factura:

    def __init__(self,name,entrega,destinatario,encargado,cantidad):
        self.name = name
        self.entrega = entrega
        self.destinatario = destinatario
        self.encargado = encargado
        self.cantidad = cantidad

    
    def getName(self):
        return self.name
    
    def getFechaEntrega(self):
        return self.entrega
    
    def getDestinatario(self):
        return self.destinatario
    
    def getEncargado(self):
        return self.encargado
    
    def getCantidad(self):
        return self.cantidad