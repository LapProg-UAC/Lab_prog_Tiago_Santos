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

    def test_funcao_casos_grandes(self):
        """Testa casos com valores maiores de n para verificar a eficiência da função"""
        self.assertEqual(funcao(10), 2 * funcao(8) + funcao(9))  
        self.assertEqual(funcao(20), 2 * funcao(18) + funcao(19))
    
    def test_funcao_casos_extremos(self):
        """Testa casos extremos para verificar o comportamento da função em limites superiores"""
        self.assertEqual(funcao(30), 2 * funcao(28) + funcao(29))  
        self.assertEqual(funcao(50), 2 * funcao(48) + funcao(49))

    def test_funcao_casos_aleatorios(self):
        """Testa casos aleatórios para verificar a consistência da função"""
        self.assertEqual(funcao(7), 2 * funcao(5) + funcao(6))  
        self.assertEqual(funcao(15), 2 * funcao(13) + funcao(14))

if __name__ == '__main__':
    unittest.main()