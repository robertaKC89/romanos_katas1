#RESUMEN: CON LOS TEST NO ME PREOCUPO DE PASAR TODAS LAS PRUEBAS DE MIS PROGRAMAS DE FORMA MANUAL!!!

#importo de la libreria python la herramienta unittest
import unittest
#desde mi archivo romanus importo la funcion que quiera utilizar para que Python interprete y la pueda probar
from romanus import convertir_en_numero

#voy a crear una class (RomanusTest) que hereda de una class genérica de la librería unittest que se llama .TestCase
#voy a poder pasar aserciones para, pasando datos poder comparar si mayor que, igual, si hay error,etc.
#defino por ejemplo una coleccion de test_unidades para comprobar si he definido bien mis unidades
#como REGLA las class acaben en test y los métodos que ejecuto empiezan por test
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

#defino otro test
    def test_numeros_basicos(self):
        self.assertEqual(convertir_en_numero("IV"), 4)
        self.assertEqual(convertir_en_numero("IX"), 9)
        self.assertEqual(convertir_en_numero("XL"), 40)
        self.assertEqual(convertir_en_numero("CCV"), 205)
        self.assertEqual(convertir_en_numero("MCXXIII"), 1123)

# defino otro test para casos anómalos (puestos en romanus.py para detectar ValueError)
# pongo assertRaises y me pide: ValueError, función, parámetro. 
    def test_no_resta_mas_de_un_orden_de_magnitud(self):
        self.assertRaises(ValueError, convertir_en_numero, "IC")
        self.assertRaises(ValueError, convertir_en_numero, "VC")
    
# defino otro test para casos anómalos
# también puedo invertir el orden definiendo 1º test que se que mi programa tiene que hacer que funcione
# es técnica TDD = desarrollo basado en problemas
# 1º generas la prueba, compruebas que falla y luego haces el programa que arregla este problema
    def test_no_restas_signos_multiplos_de_cinco(self):
        self.assertRaises(ValueError, convertir_en_numero, "VX")
      

# si me llamas desde la linea de comandos tira para adelante el metodo main desde esta libreria para cojer las clases tipo test y ejecutarlos
# método __main__ es el nombre que Python le da siempre al 1r archivo que llamo esde la línia de comandos
# si el archivo lo llamo desde una importación se llamará por su nombre: Ej. import marta = nombre marta
# si pongo condicion name == main significa que solo quiero que se ejecute si es el 1r archivo, sino no se ejecutará 
if __name__ == '__main__':
    unittest.main()


