#importo de la libreria python la herramienta unittest
import unittest
#desde mi archivo romanus importo la funcion que quiera utilizar para que Python interprete toda y la pueda probar
from romanus import convertir_en_numero

#voy a utilizar una class que hereda de una class genérica de la librería unittest que se llama .TestC
#voy a poder pasar aserciones para, pasando datos poder comparar si mayor que, igual, si hay error,etc.
#defino por ejemplo una coleccion de test_unidades para comprobar si he definido bien unidades
class RomanusTest (unittest.TestCase):
    def test_unidades (self):
    #defino para ver si un resultado es igual a algo que yo conozca-> ejemplo I = 1
        self.assertEqual (convertir_en_numero('I'), 1)
        self.assertEqual (convertir_en_numero('V'), 5)
        self.assertEqual (convertir_en_numero('X'), 10)
        self.assertEqual (convertir_en_numero('L'), 50)
        self.assertEqual (convertir_en_numero('C'), 100)
        self.assertEqual (convertir_en_numero('D'), 500)
        self.assertEqual (convertir_en_numero('M'), 1000)

# si me llamas desde la linea de comandos ejecuta el metodo main desde esta libreria para cojer las clases tipo test y ejecutarlos
if __name__ == '__main__':
    unittest.main()

