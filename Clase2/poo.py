"""
Clase persona que contenga atributos como DNI,NOMBRE,EDAD
Metodos: Setters, Getters, Constructor, Si es mayor, Mostrar
"""

class persona:
    #Constructor, con sus atributos
    def __init__(self,nom,edad,dni):
        self.nom = nom
        self.edad = edad
        self.dni = dni
    #Setters ------------------
    def setNombre(self,nom):
        self.nom = nom

    def setEdad(self,edad):
        self.edad = edad

    def setDni(self,dni):
        self.dni = dni

    #Getters ------------------
    def getNombre(self):
        return self.nom

    def getEdad(self):
        return self.edad

    def getDni(self):
        return self.dni
    
    #Metodo para saber si es mayor
    def esMayor(self):
        if(self.edad >= 18):
            return True
        else:
            return False
        
    #Metodo para mostrar los datos de la persona
    def mostrar(self):
        print(f" Persona: {self.nom}\n",f"Edad: {self.edad}\n", f"Dni: {self.dni}")
        
persona = persona("Cesar",17,"30640838")
persona.mostrar()
