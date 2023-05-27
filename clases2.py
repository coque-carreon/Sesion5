# Crear clase de perros

class perro:
    #metodo init que sirve para inicializar valores, se le conoce como constructores
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        
    # metodo ladrar
    def ladrar(self):
        print("Guau")
        
    # método datos
    def datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}")
        
# Fin de la definición de la clase

nuevo_perro = perro("Boli", 2, "Terrier")

# Llamada al metodo ladrar

nuevo_perro.ladrar() # Guau

nuevo_perro.datos() # Nombre: Boli, Edad: 2

#Perro del vecino

perro_vecino = perro("Crokis", 14, "Pastor")

perro_vecino.ladrar()

perro_vecino.datos()
