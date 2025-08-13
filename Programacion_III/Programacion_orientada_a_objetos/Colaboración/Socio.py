class Socio:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del socio: ")
        self.antiguedad = int(input("Ingrese la antigüedad: "))

    def imprimir(self):
        print(self.nombre, "tiene una antigüedad de", self.antiguedad)

    def retornar_antiguedad(self):
        return self.antiguedad


class Club:
    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def mayor_antiguedad(self):
        print("Socio con mayor antigüedad:")
        if (self.socio1.retornar_antiguedad() >= self.socio2.retornar_antiguedad() and
            self.socio1.retornar_antiguedad() >= self.socio3.retornar_antiguedad()):
            self.socio1.imprimir()
        elif self.socio2.retornar_antiguedad() >= self.socio3.retornar_antiguedad():
            self.socio2.imprimir()
        else:
            self.socio3.imprimir()


# Bloque principal
club1 = Club()
club1.mayor_antiguedad()
