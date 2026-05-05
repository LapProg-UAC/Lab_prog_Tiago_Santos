import unittest
from projeto import funcao

class TestFuncao(unittest.TestCase):
    def test_funcao_casos_base(self):
        """Testa os casos base: n = 0 e n = 1"""
        self.assertEqual(funcao(0), 0)  
        self.assertEqual(funcao(1), 1)

    def test_funcao_valores_negativos(self):
        """Testa casos inválidos: n < 0"""
        with self.assertRaises(ValueError):
            funcao(-1)
        with self.assertRaises(ValueError):
            funcao(-6)
    
    def test_funcao_casos_gerais(self):
        """Testa casos gerais: n > 1"""
        self.assertEqual(funcao(2), 2 * funcao(0) + funcao(1))  
        self.assertEqual(funcao(5), 2 * funcao(3) + funcao(4))

if __name__ == '__main__':
    unittest.main()