#importo de la libreria python la herramienta unittest
import unittest
#desde mi archivo romanus importo la funcion que quiera probar
from romanus import convertir_en_numero

#voy a utilizar una class que hereda de una class genérica de la librería unittest que se llama .TestC
#voy a poder pasar aserciones para, pasando datos poder comparar si mayor que, igual, si hay error,etc.
#defino por ejemplo una coleccion de test_unidades para comprobar si he definido bien unidades
class RomanusTest (unittest.TestCase):
    def test_unidades (self):
    #defino para ver si un resultado es igual a algo que yo conozca-> I = 1
        self.assertEqual (convertir_en_numero('I'), 1)
