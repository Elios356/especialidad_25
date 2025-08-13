class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def mostrar_perimetro(self):
        perimetro = self.lado * 4
        print("El perímetro del cuadrado es", perimetro)

    def mostrar_superficie(self):
        superficie = self.lado * self.lado
        print("La superficie del cuadrado es", superficie)

# Bloque principal
cuadrado1 = Cuadrado(10)
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()
