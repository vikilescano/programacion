#TESTS
import unittest
from semana_02 import (
    invertir_lista,
    collatz,
    contar_definiciones,
    cantidad_de_claves_letra,
    propagar,
)
##Ejercicio 1

class TestInvertirLista(unittest.TestCase):
    def test_numeros(self):
        self.assertEqual(invertir_lista([0.1, 2, 0.3]), [0.3, 2, 0.1])

    def test_negativos(self):
        self.assertEqual(invertir_lista([-10, -20, -30]), [-30, -20, -10])

    def test_ciudades(self):
        self.assertEqual(
            invertir_lista(['Bogotá', 'Rosario', 'San Fernando', 'San Miguel']),
            ['San Miguel', 'San Fernando', 'Rosario', 'Bogotá']
        )

    def test_lista_vacia(self):
        self.assertEqual(invertir_lista([]), [])

    def test_un_numero(self):
        self.assertEqual(invertir_lista([42]), [42])


##Ejercicio 2

class TestCollatz(unittest.TestCase):
   def test_cero(self):
    with self.assertRaises(ValueError):
        collatz(0)

    def test_impar(self):
        self.assertEqual(collatz(19), 20)

    def test_par(self):
        self.assertEqual(collatz(120), 20)
    
    def test_negativo(self):
        with self.assertRaises(ValueError):
         collatz(-120)

    def test_lista(self):
        with self.assertRaises(ValueError):
         collatz([10])


##Ejercicio 3

class TestDiccionarios(unittest.TestCase):
    def test_contar_definiciones_usual(self):
        d = {"A": [1, 2], "B": ["x"], "C": []}
        esperado = {"A": 2, "B": 1, "C": 0}
        self.assertEqual(contar_definiciones(d), esperado)

    def test_contar_definiciones_vacio(self):
        self.assertEqual(contar_definiciones({}), {})


    def test_cantidad_de_claves_letra_usual(self):
        d = {"Hola": [], "Hugo": [], "Casa": []}
        self.assertEqual(cantidad_de_claves_letra(d, "H"), 2)

    def test_cantidad_de_claves_letra_0(self):
        d = {"A": [], "B": []}
        self.assertEqual(cantidad_de_claves_letra(d, "Z"), 0)

    def test_cantidad_de_claves_mayuscula(self):
        d = {"hola": [], "Hola": []}
        self.assertEqual(cantidad_de_claves_letra(d, "H"), 1)

##Ejercicio 4

class TestPropagar(unittest.TestCase):
    def test_propagar_normal(self):
        self.assertEqual(propagar([0, 0, 0, 1, 0, 0]), [1, 1, 1, 1, 1, 1])

    def test_todo_carbonizado(self):
        self.assertEqual(propagar([-1, -1, -1]), [-1, -1, -1])

    def test_todo0(self):
        self.assertEqual(propagar([0, 0, 0]), [0, 0, 0])

    def test_borde(self):
        self.assertEqual(propagar([1, 0, 0]), [1, 1, 1])

if __name__ == '__main__':
    unittest.main()
