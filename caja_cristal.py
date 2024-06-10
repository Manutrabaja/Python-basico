import unittest


def es_adulto(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    pass 

    def test_es_aldulto(self):
        edad = 20
        resultado = es_adulto(edad)

        self.assertEqual(resultado, True)

    def test_es_menor(self):
        edad = 15
        resultado = es_adulto(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()
