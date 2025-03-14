# Composicion

"una coordenada en 2 direcciones esta compuesta por 2 valores, el valor en el eje de las X y el valor en el eje de las Y, esto podria ser una clase. Un cuadrado esta compuesto por 4 coordenadas que son los 4 vertices, Esto podria ser una clase qeu esta compuesta por 4 clases del objeto coordenada."

# Clase coordenada

class Coordenada:
    #METODO CONSTRUCTOR
    def __init__(self,x,y):
        self.X = x
        self.Y = y

        # metodo para mostrar coordenada
    def MostrarCoordenada(self):
        print("(",self.X, ",", self.Y, ")")

# Clase cuadrado 
class Cuadrado:
    #metodo constructor
    def __init__(self, v1,v2,v3,v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # metodo para mostrar los vertices
    def MostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.V1.MostrarCoordenada()
        self.V2.MostrarCoordenada()
        self.V3.MostrarCoordenada()
        self.V4.MostrarCoordenada()

# Metodo Principal
def main():
    #input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("digite el valor de y: "))

    c1 = Coordenada(x1,x2)
    c1.MostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    Cuadrado1 = Cuadrado(v1,v2,v3,v4)
    Cuadrado1.MostrarVertices()

if __name__ == "__main__":
    main()
        
