import unittest
from src.validacion import (
    validar_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestValidacionNumeros(unittest.TestCase):
    def test_numero_valido(self):
        numero = validar_numero("50")
        self.assertEqual(numero, 50)

    def test_numero_cero(self):
        with self.assertRaises(NumeroDebeSerPositivo):
            validar_numero("0")

    def test_numero_negativo(self):
        with self.assertRaises(NumeroDebeSerPositivo):
            validar_numero("-25")

    def test_input_no_valido(self):
        with self.assertRaises(ValueError):
            validar_numero("texto")

    def test_input_vacio(self):
        with self.assertRaises(ValueError):
            validar_numero("")

if __name__ == '__main__':
    unittest.main()
