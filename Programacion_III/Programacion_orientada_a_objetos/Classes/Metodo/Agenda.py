class Agenda:
    def __init__(self):
        self.contactos = {}

    def menu(self):
        opcion = 0
        while opcion != 5:
            print("1 - Carga de un contacto en la agenda")
            print("2 - Listado completo de la agenda")
            print("3 - Consulta ingresando el nombre de una persona")
            print("4 - Modificación del teléfono y mail")
            print("5 - Finalizar el programa")
            opcion = int(input("Ingrese su opción: "))
            
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listado()
            elif opcion == 3:
                self.consulta()
            elif opcion == 4:
                self.modificacion()

    def cargar(self):
        nombre = input("Nombre de la persona: ")
        telefono = input("Teléfono: ")
        mail = input("Mail: ")
        self.contactos[nombre] = (telefono, mail)
        print("--------------------")

    def listado(self):
        print("Listado de la agenda")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0], self.contactos[nombre][1])
        print("--------------------")

    def consulta(self):
        nombre = input("Ingrese el nombre de la persona a consultar: ")
        if nombre in self.contactos:
            print(nombre, "su teléfono es", self.contactos[nombre][0],
                  "y su mail es", self.contactos[nombre][1])
        else:
            print("No existe un contacto con dicho nombre")

    def modificacion(self):
        nombre = input("Ingrese el nombre de la persona a modificar su teléfono y mail: ")
        if nombre in self.contactos:
            telefono = input("Ingrese nuevo teléfono: ")
            mail = input("Ingrese el nuevo mail: ")
            self.contactos[nombre] = (telefono, mail)
        else:
            print("No existe un contacto con dicho nombre")

# Bloque principal
agenda = Agenda()
agenda.menu()
