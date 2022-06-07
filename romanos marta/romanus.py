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
# Ya tenemos la descomposición, SE PODRÁ ACCEDER POR POSICIÓN PARA CONVERTIR A TEXTO ROMANO!
# Se plantea una LISTA:
    millares = [ "", "M", "MM", "MMM" ]
    centenas = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
    decenas = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
    unidades = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]
#HAGO UNA LISTA DE LISTAS (conversores tiene 4 listas)
    conversores = [millares, centenas, decenas, unidades]

#UNA DE LAS OPCIONES QUE NOS PUEDE SERVIR PARA VALIDAR ENTRADA
    #try:
    #    numero_validado = int (numero)
    #except ValueError:
    #    raise ValueError (f'{numero} no es num valido')

#OTRA OPCIÓN QUE NOS PUEDE SERVIR PARA VALIDAR ENTRADA
    # if numero > 0 and numero < 4000:
    #     return 'OK'
    # return 'el num no es valido, debe ser positivo y menor que 4000'

#OTRA OPCION PARA VALIDAR ENTRADA Y USAMOS ESTA!!! Pero convirtiendo a not para ahorrarme el else
    if not isinstance(numero, int):
        return "No has introducido un número"
    if numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor que 4000)"

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
        factores.append(cociente)
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

#la posicion corresponde al conversor que debo acceder de lista de listats conversores de arriba
#el resultado se que es cadena, por lo que la dejo vacía y ya veré que pinto de valores
#enumerate útil xk devuelve TUPLA con un contador que empieza en 0 y los valores del objeto iterable
    resultado = ''
    for pos, factor in enumerate(factores):
        resultado = resultado + conversores[pos][factor]
    return resultado

#otra manera de acceder por posición-> resultado de ej.'millares' por lo que tenga en posición de factores
    #r_millares = millares [factores [0]] 
    #r_centenas = centenas [factores [1]]
    #r_decenas = decenas [factores [2]]
    #r_unidades = unidades [factores [3]]

    #return f'{r_millares} {r_centenas} {r_decenas} {r_unidades}'

# y llamo a la función para comprobar si funciona con cualquier num
print (convertir_en_romano (3))
print (convertir_en_romano (555))
print (convertir_en_romano (208))
print (convertir_en_romano (22))

#AL FINAL HEMOS COMPRIMIDO LA FUNCION AL MÁXIMO CON LISTAS YA QUE ESTAMOS ANTE SISTEMAS DE NUMEROS POSICIONALES Y LO MÁS FÁCIL ES LISTA. 

# ------------------------------------- PRIMERA MITAD DEL PROGRAMA CONVERSION ENTERO A ROMANO HECHA --------------------------------

def convertir_en_numero (romano):
    """
    MCXXIII: 1123
        - de izquierda a derecha -> lo hago con el bucle for
        - convertir cada letra en su valor -> lo hago con el diccionario
        - sumo los valores si a la izquierda hay un dígito mayor que a la derecha
            - VI: sumo ==> 6
        - resto si el valor de la izquierda es menor que el de la derecha
            - IV: resto ==> 4

        1. leo una letra y guardo su valor (letra1)
        2. leo otra letra (letra2)
            2a. si letra2 > letra1 =>  resultado = letra2 - letra1
            2b. si no => resultado letra2 + letra1
    """
    #1º ME DEFINO DICCIONARIO PARA ACCEDER POR KEY
    digitos_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    resultado = 0
    anterior = 0
    #recorro la cadena para llevarla a num.y esta coincide con la key de mi diccionario y luego me irá sumando a resultado la iteracion de cada letra que le asigna el valor
    #lo que hago todo el rato es comparar las letras de dos en dos y guardando anterior para ver si sumo o resto con el valor actual
    for letra in romano:
        actual = digitos_romanos [letra]
        if anterior >= actual:
            resultado = resultado + actual
        else:
        #valido si resta es posible ya que no puedo restar si hay más de un orden de magnitud entre anterior y actual
        #no puedo restar de ud a centenas por ejemplo ya que hay más de un orden de magnitud.  
        #10  10  10  10 -> dato imp. es que entre magnitudes se llevan 10!
        #1123 = 1*10^3 + 1*10^2 + 2*10^1 + 3*10^1 = 1000 + 100 + 20 + 3
        #estoy en el punto de que anterior < actual
        #COMPROVACIONES QUE FUNCIONAN Y QUE NO:
         #si: IV  ---   anterior=1,   actual=5         1*10 ---- 5
         #si: IX  ---   anterior=1,   actual=10        10 ---- 10
         #si: CM  ---   anterior=100, actual=1000    1000 ---- 1000
         #no: IC  ---   anterior=1,   actual=100      10 ---- 100
         #no: XM  ---   anterior=10,  actual=1000    100 ---- 1000
         #no: I   ---   anterior=0,   actual=1         0 ---- 1
         #no: X   ---   anterior=0,   actual=10        0 ---- 10

        # IV -> otra opción de operación aritmética:
         # anterior=0, actual=1 ----    0 <= 1 ////  1 - 0 > 0
         # anterior=1, actual=5         0 <= 10 //// 10 > 0

        # actual - anterior*10 (para compararlos y ver si puedo restar) ---> si cero o negativo OK
        #                                                               ---> si positivo KO
        # imp.! anterior *10 siempre será cero ya que es el primero que entra al validador, por lo que hau que meterlo en la condicion 
        # es decir, con 3 valores a comparar busco la condicion de error y si no salta hará la resta:
            if anterior > 0 and anterior*10 > actual:
                raise ValueError ('no se puede restar mas de un orden de magnitud')
                
            resultado = resultado - anterior
            resultado = resultado + (actual - anterior)
        anterior = actual  
    return resultado 
print (convertir_en_numero ('IC'))





        # if (actual - anterior*10) > 0:
        # if anterior > 0 and anterior*10 < actual:
        # if anterior*10 > 0 and anterior*10 < actual:

        # if anterior == 5 or anterior == 50 or anterior == 500:

