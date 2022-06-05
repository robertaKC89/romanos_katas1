# funcion que me debe convertir numero en romano
def convertir_en_romano(numero):
    """
    ->Restricciones:
        - Es un número natural
        - El número está entre 0 y 3999
        - no es negativo
        - no es mayor que 3999
    Resultado es una cadena que contiene (I, V, X, L, C, D, M)
    
    ->Ideas para comprobar un entero:
        - (X) isdigit(): porque no aplica a cualquier cosa que no sea cadena
        - (V) convertir a int y si no se puede, error
        - (V) isinstance()
        - (V) type()
        - (X) isnumeric()

    ->Pasos:
        1. Validar la entrada
        2a. Si es válido: lo convierto
        2b. Si no es válido ya no sigo: muestro un error
    """

#ESTA ES UNA DE LAS OPCIONES QUE NOS PUEDE SERVIR
    #try:
    #    numero_validado = int (numero)
    #except ValueError:
    #    raise ValueError (f'{numero} no es num valido')

#ESTA ES OTRA OPCIÓN QUE NOS PUEDE SERVIR
    # if numero > 0 and numero < 4000:
    #     return 'OK'
    # return 'el num no es valido, debe ser positivo y menor que 4000'

#ESTA ES OTRA OPCION BUENA Y NOS QUEDAMOS CON ESTA!!! Pero convirtiendo a not para ahorrarme el else
    if not isinstance (numero, int):
        return 'no has introducido un numero' 
    if numero < 1 or numero > 3999:
        return 'el num no es válido. debe ser mayor que uno y menor que 4000'

#llamo a la funcion para utilizarla (ojo con restricciones, no pondré print'a' o '-3' xk me dará error)
#print (convertir_en_romano (9000))
#print (convertir_en_romano (3))

# SIGUIENTE PASITO ES DESCOMPONER 'numero' en UD, DECENTAS, CENTENAS Y UD. DE MILLAR
# opcion 1: division entera + módulo o residuo en cascada 
# opcion 2: convertir en cadena y en funcion de longitud y posición obtener ud, d, c, y ud. millar 
# IMP. El formato me tiene que servir para todos igual!

# opcion 1: division entera + módulo/residuo en cascada: 
    divisores = [1000, 100, 10, 1]
    factores = [] 
    for divisor in divisores:
        cociente = numero // divisor 
        resto = numero % divisor
        factores.append (cociente)
        numero = resto 
    
#CON EL FOR ESTAMOS ITERANDO DE LA SIGUIENTE MANERA (podría hacerse con while tambien): 
#1123 / 1000 = 1  >>>> he impreso este valor
#1123 % 1000 = 123 
#123 / 100= 1 >>>>> he impreso este valor
#123 % 100= 23
#23 / 10 = 2 >>>>> he impreso este valor 
#23 % 10 = 3
#3 / 1 = 3 >>>>> he impreso este valor 
#3 % 1 = 3

# Ya tenemos la descomposición, AHORA VAMOS A ACCEDER POR POSICIÓN PARA CONVERTIR A TEXTO ROMANO!
# Se plantea una LISTA:
    millares = [ "", "M", "MM", "MMM" ]
    centenas = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
    decenas = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
    unidades = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]

#accediendo por posición quedaria -> resultado de ej.'millares' por lo que tenga en posición de factores
    r_millares = millares [factores [0]] 
    r_centenas = centenas [factores [1]]
    r_decenas = decenas [factores [2]]
    r_unidades = unidades [factores [3]]

    return r_millares + r_centenas + r_decenas + r_unidades

# y llamo a la función para comprobar si funciona con cualquier num
print (convertir_en_romano (3))
print (convertir_en_romano (555))
print (convertir_en_romano (2788))
print (convertir_en_romano (22))
