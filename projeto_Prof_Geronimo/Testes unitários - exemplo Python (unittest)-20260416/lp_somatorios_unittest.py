import unittest
from lp_somatorios import lista_somas

class TestListaSomas(unittest.TestCase):
    def test_somas_negativo(self) -> None:
        """
         Caso inválido: n = -1 (< 0)
        :return: None
        """
        with self.assertRaises(ValueError):
            lista_somas(-1)

    def test_somas_zero(self) -> None:
        """
        Caso inicial: n = 0
        :return: None
        """
        self.assertEqual(lista_somas(0), [0])

    def test_somas_positivo(self) -> None:
        """
        Primeiras somas: n = 1, 2, ...
        :return: None
        """
        self.assertEqual(lista_somas(1), [0, 1])
        self.assertEqual(lista_somas(2), [0, 1, 3])

if __name__ == '__main__':
    unittest.main()
