# Clase base 1
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

# Clase base 2
class Volador:
    def volar(self):
        print(f"{self.nombre} está volando.")

# Clase base 3
class Nadador:
    def nadar(self):
        print(f"{self.nombre} está nadando.")

# Clase que usa herencia múltiple
class Pato(Animal, Volador, Nadador):
    def __init__(self, nombre):
        # Llamar al constructor de la clase Animal
        Animal.__init__(self, nombre)

# Crear un objeto de la clase Pato
pato = Pato("Buche perra")

# Usar métodos de todas las clases base
pato.dormir()     # Método de la clase Animal
pato.volar()      # Método de la clase Volador
pato.nadar()      # Método de la clase Nadador
