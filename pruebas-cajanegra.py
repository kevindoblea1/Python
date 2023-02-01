"""Pruebas de caja negra"""
import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):
    def test_suma_positivos(self):
        num_1 = 10
        num_2 = 20

        resultado = suma(num_1, num_2)
        
        self.assertEqual(resultado, 30)

    def test_suma_negativos(self):
        num_1 = -10
        num_2 = -7
        
        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__ == '__main__':
    unittest.main()



