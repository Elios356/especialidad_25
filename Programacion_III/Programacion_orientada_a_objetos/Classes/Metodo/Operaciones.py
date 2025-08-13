class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))

    def sumar(self):
        suma = self.valor1 + self.valor2
        print("La suma es", suma)

    def restar(self):
        resta = self.valor1 - self.valor2
        print("La resta es", resta)

    def multiplicar(self):
        multi = self.valor1 * self.valor2
        print("El producto", multi)

    def dividir(self):
        divi = self.valor1 / self.valor2
        print("La división", divi)

# Bloque principal
operacion1 = Operaciones()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.dividir()
