# poo_python

- El paradigma de POO esta basado en una abstraccion del mundo real que nos va a permitir desarrollar programas de forma ms cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## Clase

- una clase es un tipo de dato cullas variables se llaman objetos o instancias.
- La clase es la definicion del concepto del mundo real y los objetos o instancias  son el propio objeto del mundo real.
- Las clases estan compuestan por dos elementos: atributos y metodos 

### Atributos

- Los atributos son informacion que almacena la clase.

### Métodos

- Las operaciones que pueden realizar las clases.

## Definicion de una clase en python

```Python
class NombreClase:
def __Init__(self, variable1,variable2:)
    self.atributo1 = valor1
    self.atributo2 = valor 2

def NombreMetod(self):
    bloque de codigo
 ```
 ### Componentes

 - ```class```: palabra reservada en python para definir una clase.
 - ```NombreClase```: nombre de la clase que quieres crear.
 - ```def```: palabra reservada en python que se utiliza para definir tanto el constructor de la clase (Metodo que se ejecuta la primera vez que usas una clase) como los diferentes metodos que tiene.
- ```__init__```: palabra reservada en python para definir el metodo construcctor de la clase. es lo primero que se ejecuta cuando creas un objeto de una clase.
- ```self, variableX```: parametro del construcctor de la clase.El parametro self es obligatorio y despues puedes tener tantos parametros como quieras, la forma de añadir parametros es la misma que en las funciones.
- ```self.atributoX```: forma de utilizacion y acceso a los atributos de la clase.
```nombreMetodo```: nombre del metodo de la clase.
- ```(self)```: parametros del metodo. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras, la forma de añadir parametros es la misma que en las funciones.
- ```bloqueCodigo```: Instrucciones que ejecutara el metodo.

cuando defines una clase debes tener en cuenta los siguientes puntos:
- puedes definir tantos atributos como necesites.
- puedes definir tantos metodos como necesites.
- puedes tantos parametros con el constructor y en los metodos como necesites.

## Composicion

- Consiste en al creacion de nuevas clases a partir de otras clases ya existentes que actuan como elementos compositores de la nueva.
- LAs clases existentes seran atributos de la nueva clase.
-  En POO la composicion significa que entre las 2 clases existe una relacion del tipo "Tiene un".
- Ejemplo:
    - una coordenada en 2 direcciones esta compuesta por 2 valores, el valor en el eje de las X y el valor en el eje de las Y, esto podria ser una clase. Un cuadrado esta compuesto por 4 coordenadas que son los 4 vertices, Esto podria ser una clase qeu esta compuesta por 4 clases del objeto coordenada.

