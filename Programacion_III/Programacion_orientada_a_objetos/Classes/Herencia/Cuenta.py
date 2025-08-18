class Cuenta:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def imprimir(self):
        print("Titular:", self.titular)
        print("Monto:", self.monto)


class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)

    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super().imprimir()


class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, interes):
        super().__init__(titular, monto)
        self.plazo = plazo
        self.interes = interes

    def imprimir(self):
        print("Cuenta de plazo fijo")
        super().imprimir()
        print("Plazo en días:", self.plazo)
        print("Intereses:", self.interes)
        self.ganancia()

    def ganancia(self):
        gan = self.monto * self.interes / 100
        print("Monto de interés:", gan)


# ---------------------
# PRUEBAS DE EJEMPLO
# ---------------------

print("== Cuenta Caja de Ahorro ==")
caja = CajaAhorro("Ana", 1500)
caja.imprimir()

print("\n== Cuenta Plazo Fijo ==")
plazo = PlazoFijo("Luis", 5000, 30, 5)
plazo.imprimir()
