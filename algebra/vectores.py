"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Arnau piñero Masegosa

    Tests unitarios de las funciones desarrolladas:

    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])
    >>> v1 * v2
        Vector([4, 10, 18])
    >>> v1 * 2
        Vector([2, 4, 6])
    
    >>> v1 @ v2
        32
    
    >>> v1 = Vector([2, 1, 2])
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> v1 // v2 
        Vector([1.0, 2.0, 1.0])
    >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    

    def __mul__(self, other):
        """
        Producto de Hadamard entre vectores, o producto de un vector por un escalar
        """

        if isinstance(other, Vector):
            if len(self.item) != len(other.item):
                raise ValueError("Los vectores deben tener la misma longitud")
            return Vector([x * y for x, y in zip(self.item, other.item)])
        elif isinstance(other, (int, float)):
            return Vector([x * other for x in self.item])
        else:
            raise TypeError("El producto debe ser con un vector o un escalar")
        
    def __rmul__(self, other):
        """
        Método reflejado del producto por un escalar o de Hadamard
        """

        return self.__mul__(other)
    
    def __matmul__(self, other):
        """
        Producto escalar de dos vectores
        """

        if isinstance(other, Vector):
            if len(self.item) != len(other.item):
                raise ValueError("Los vectores deben tener la misma longitud")
            return sum([x * y for x, y in zip(self.item, other.item)])
        else:
            raise TypeError("El producto escalar debe ser con un vector")
        
    def __rmatmul__(self, other):
        """
        Método reflejado del producto escalar
        """

        return self.__matmul__(other)
    
    def __floordiv__(self, other):
        """
        Método que devuelve la componente tangencial (paralela) de un vector respecto a otro
        """
        import math

        if isinstance(other, Vector):
            if len(self.item) != len(other.item):
                raise ValueError("Los vectores deben tener la misma longitud")
            prod_escalar = self.__matmul__(other)
            magnitud = math.sqrt(sum(x ** 2 for x in other.item))
            return Vector([prod_escalar / magnitud ** 2 * x for x in other.item])
        else:
            raise TypeError("La componente tangencial debe ser con un vector")

    def __rfloordiv__(self, other):
        """
        Metodo reflejado de la componente tangencial
        """

        return self.__floordiv__(other)
    
    def __mod__(self, other):
        """
        Metodo de calculo de la componente normal (perpendicular) de un vector respecto a otro
        """

        if isinstance(other, Vector):
            if len(self.item) != len(other.item):
                raise ValueError("Los vectores deben tener la misma longitud")
            paralelo = self.__floordiv__(other)
            normal = [x - y for x, y in zip(self.item, paralelo)]
            return Vector(normal)
        else:
            raise TypeError("La componente normal debe ser con un vector")

    def __rmod__(self, other):
        """
        Metodo reflejado de la componente normal
        """
        
        return self.__mod__(other)


