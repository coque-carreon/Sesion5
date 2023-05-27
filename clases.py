# Definición de clase

class Auto:
    def __init__(self):
        self.color = "Rojo" # Queda dentro de la clase
        #marca = "VW" # Es una variable local, no de clase
        self.marca = "VW"
        
# Crear objeto a partir de clase Auto
auto_coque = Auto()
print(auto_coque.color) # Rojo
print(auto_coque.marca) # ¿? Marca no xiste dentro del objeto, luego al cambiarlo a selg se convierte en parte de la clase

