#Ejercicio 1
#Entradas: El radio del círculo
#Salidas: Un diccionario que contiene el área y la circunferencia del círculo, etiquetados como Area y Circunferencia respectivamente
#Restricciones: El radio debe estar en los números reales
#Herramientas: Python, la fórmula de la circunferencia y el área, operaciones matemáticas
'''La función calcula la circunferencia y el área del círculo cuyo radio recibe, para esto se utilizan las fórmulas de la circunferencia (2 * pi * radio) 
y el área (pi * radio^2) respectivamente, instantaneamente se crea una variable que contiene el valor de pi para realizar estos cálculos. 
Estos datos se almacenan en variables llamadas area y circunferencia y luego añadidas a un diccionario con las etiquetas Area y Circunferencia, 
en cada una se guarda su dato respectivo y esto es lo que la función devuelve al final de su funcionamiento. '''

def circulo(radio):
    pi = 3.141592653589793

    area = pi * radio**2
    circunferencia = 2 * pi * radio

    return {'Area': area, 'Circunferencia': circunferencia}

#Ejercicio 3
#Entradas: El radio de la esfera
#Salidas: Un diccionario que contiene el volumen y área de una esfera.
#Herramientas: Python, fórmula del volumen y el área de la esfera, operaciones matemáticas
'''Esta función recibe el radio de una esfera para calcular su volumen y área con las fórmulas respectivas para cada uno de esos valores: 4/3 * pi * radio^3 para el área y 4 * pi * radio^2. 
El valor de pi está guardado en una variable del mismo nombre con sus primeros 15 decimales. 
La variable realiza los cálculos correspondientes con las fórmulas dadas y los guarda en variables para el área y el volumen (con los mismo nombres) que posteriormente son añadidos 
a un diccionario con etiquetas que corresponden a cada uno de los datos.'''

def esfera(radio):
    pi = 3.141592653589793

    area = 4 * pi * radio**2
    volumen = 4/3 * pi * radio**3

    return {'area': area, 'volumen': volumen}

#Ejercicio 5
#Entradas: Un número entero que representa un año.
#Salidas: Un valor booleano dependiendo de si el año es bisiesto o no.
#Restricciones: Dado a que el número que entra representa un año, este debe ser un número entero positivo
#Herramientas: Python, estructuras de decisión, módulo
'''La función recibe un número entero positivo que representa un año, esta función analiza si ese número es divisible por 4 a la vez que no es divisible por 100. 
En caso de cumplir esta condición retorna el valor de True, en caso contrario, ahora evalúa si es divisible entre 400, en caso de serlo devuelve True, si no lo es entonces devuelve False.'''

def bisiesto(anio):

    if anio % 4 == 0 and anio % 100 != 0:
        return True
    elif anio % 400 == 0:
        return True
    else:
        return False

#Ejercicio 7
#Entradas: 3 números
#Salidas: El mediano de los 3 números
#Restricciones: Los 3 números deben pertenecer a los números reales
#Herramientas: Python, estructuras de desición, operadores de comparación.
'''La función recibe 3 números y mediante operaciones de comparación, se obtiene cuál es el mediano de los 3 números. Esto se hace comparando los escenarios en los que los 3 números pueden ser
el mediano que son 2 por número hasta que se cumple alguno y lo devuelve'''

def mediano(a, b, c):
    if b < a < c or c < a < b:
        return a
    elif a < b < c or c < a < b:
        return b
    else:
        return c

#Ejercicio 9
#Entradas: Capacidad en gigabytes de un disco duro
#Salidas: Esa capacidad pero en bytes
#Restricciones: Dado a que estamos hablando de una medida, esta debería ser un número real positivo
#Herramientas: Python, fórmulo para hacer la conversión, operaciones matemáticas.
'''El funcionamiento de esta subrutina consiste en recibir la capacidad en gigabytes de un disco duro como entrada y convertirla a bytes. Esto se puede realizar fácilmente mediante la fórmula 
capacidad * 1024^3, Finalmente devuelve la capacidad del disco en bytes'''

def disco(capacidad):
    capacidad_bytes = capacidad * 1024**3

    return capacidad_bytes

#Ejercicio 11
#Entradas: Un número que representa una distancia dada en metros y un número entero entre 1 y 4 que representa la unidad a convertir la medida dada, siendo estas: 1: Centimentros. 2: Pulgadas.
#3: Pies. 4: Yardas
#Salidas: Esa cantidad en la unidad seleccionada mediante la entrada del número que lo indica.
#Restricciones: El número que indica el tipo debe ser un número entero entre 1 y 4.
#Herramientas: Python, fórmulas de conversión, operaciones matemáticas.
'''Esta función recibe una cantidad dada en metros la cual es convertida a centimetros, pulgadas, pies o yardas; esto debido a que las fórmulas usadas dependen de estas conversiones entre ellas
(con excepción de la fórmula para convertir a cm) para poder hacer los cálculos. Luego dependiendo del número en la entrada del tipo, devuelve la conversión deseada'''

def convertir(distancia, tipo):
    centimetros = distancia * 100
    pulgadas = centimetros / 2.54
    pies = pulgadas / 12
    yardas = pies / 3

    if tipo == 1:
        return centimetros
    elif tipo == 2:
        return pulgadas
    elif tipo == 3:
        return pies
    else:
        return yardas

#Ejercicio 13
#Entradas: Número que representa el salario actual del jugador.
#Salidas: Una tupla que contiene el nuevo salario aumentado y el porcentaje de aumento.
#Restricciones: El salario debe ser mayor o igual a 0
#Herramientas: Python, operaciones matemáticas para obtener la cantidad de aumento de acuerdo al porcentaje determinado, estructuras de desición.
'''La función toma el valor del salario y en función del rango en el que se encuentre se le aplica un determinado aumento. Si se encuentra entre 0 y 1000000, el aumento es del 20%. Si está entre 
1000001 y 1500000, se aplica un aumento del 10%. Un salario de entre 1500001 y 2000000 recibe un aumento del 5%. Finalmente un salario de más de 2000000'''

def aumento(salario):

    if 0 <= salario <= 1000000:
        salario += salario * 0.20
        return (salario, 20)
    elif 1000001 <= salario <= 1500000:
        salario += salario * 0.10
        return (salario, 10)
    elif 1500001 <= salario <= 2000000:
        salario += salario * 0.05
        return (salario, 5)
    else:
        return (salario, 0)

#Ejercicio 15
#Entradas: Un número entero
#Salidas: Un valor booleano que indica si el número es un palíndromo (True) o no (False)
#Restricciones: El número debe pertenecer a los números enteros
#Herramientas: Python, operaciones matemáticas, estructuras de desición y repetición.
'''Para esta función se crea una variable para almacenar el dato de entrada, esto porque por la manera en la que la función realiza su trabajo, se requiere modificar el número original. 
Se utiliza un bucle en el que se saca el módulo del número de entrada, esto para poder rescatar sus dígitos poco a poco y añadirlos a una variable en la que se guarda ese número
pero invertido, luego el número de entrada es dividido de forma entera entre 10 para así poder reducirlo poco a poco hasta llegar a 0, en ese momento termina el bucle. Luego se compara el número original
y el invertido, si son iguales se devuelve un True, caso contrario devuelve un False.'''

def palindromo(numero):
    digito = 0
    invertido = 0
    num = numero

    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num //= 10

    if numero == invertido:
        return True
    else:
        return False

#Ejercicio 17
#Entradas: Un número entero y un dígito
#Salidas: El número con el dígito adjunto
#Restricciones: El número debe ser entero y el dígito también. El dígito debe ser solo uno.
#Herramientas: Python, operaciones matemáticas para añadir el dígito determinado y una fórmula para ello.
'''Esta función recibe un número y un dígito que debe adjuntar como un dígito a la derecha. Para esto se utilzará la fórmula num * 10 + dig'''

def adjunto(num, dig):
    adjunto = num * 10 + dig

    return adjunto

#Ejercicio 19
#Entradas: El radio interno (a) y el radio externo (b) de un toro (tipo de poliedro)
#Salidas: Un diccionario que contiene el área y el volumen del toro. Las etiquetas son: 'area' y 'volumen'
#Restricciones: El valor del toro debe pertenecer a los números reales
#Herramientas: Python, fórmulas para obtener el área y el volumen, operaciones matemáticas. 
'''La función recibe los valores del radio interno y el radio externo del toro y los utiliza para calcular el área y volumen de este. Esto se realiza con las fórmulas pi^2 * (b^2 - a^2) para el área 
y (pi^2*(a+b)*(b-a)^2) / 4 para el volumen. Finalmente la función devuelve ambos valores en un diccionario con las etiquetas 'area' y 'volumen' para sus respectivos datos.'''

def toro(a, b):
    pi = 3.141592653589793

    area = pi**2 * (b**2 - a**2)
    volumen = (pi**2 * (a + b) * (b - a)**2) / 4

    return {'area': area, 'volumen': volumen}

#Ejercicio 21
#Entradas: Un número entero
#Salidas: Un string con la secuencia en letras del número de entrada
#Restricciones: El número deber ser entero
#Herramientas: Python, estructuras de control y desición, división entera y módulo, subrutina length (función) y subrutina invertir (función)
'''A la función ingresa un número entero el cual lo primero que hace es ser invertido debido a que por la naturaleza de extraer los dígitos de un número, podría dar resultados incorrectos. 
Esto se hace mediante una subrutina llamada invertir, que recibe un número, le da la vuelta y lo devuelve así. Seguido de eso, poco a poco es descommpuesto usando bucle en el que al número 
se le extrae su último dígito utilizando división entera, luego se determina que número es y una vez hecho eso, se añade su nombre con un guión al final para así mantener una estructura al añadir los otros números y se divide exactamente por 10 para reducir el número en cada iteración. 
Finalmente, haciendo uso de la subrutina length para obtener la longitud del string, este string se reasigna quitando el último carácter porque este siempre es un guión haciendo uso de substrings
y se retorna el string con los números en letras'''

#Función length
#Entradas: Una secuencia
#Salidas: La longitud de la secuencia
#Restricciones: La secuencia debe ser iterable
#Herramientas: Python, bucle for, un contador y sumas
'''La función length recibe una secuencia iterable y la recorre haciendo uso de un bucle for, conforme la recorre va sumando 1 a un contador. Al final, el mismo contador se retorna con la suma 
terminada.'''

def length(secuencia):
    contador = 0

    for i in secuencia:
        contador += 1

    return contador

#Función invertir
#Entradas: Un número 
#Salidas: El mismo número pero invertido
#Restricciones: El número ingresado debe ser entero
#Herramientas: Python, división entera, módulo, multiplicación y suma.
'''Esta función recibe un número entero y lo descompone poco a poco con el uso de un bucle while, durante esta descomposición añade los dígitos a una variable mediante el uso de algunas operaciones
matemáticas, esto resulta en el mismo número pero invertido. Finalmente este número se devuelve'''

def invertir(numero):
    invertido = 0
    digito = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero //= 10

    return invertido

#Función numLetras2
#Toda la información sobre esta función está explicada al inicio del ejercicio.

def numLetras2(numero):
    digito = 0
    num_letras = ''
    invertido = invertir(numero)

    while invertido > 0:
        digito = invertido % 10
        if digito == 0:
            num_letras += 'cero-'
            invertido //= 10

        elif digito == 1:
            num_letras += 'uno-'
            invertido //= 10

        elif digito == 2:
            num_letras += 'dos-'
            invertido //= 10

        elif digito == 3:
            num_letras += 'tres-'
            invertido //= 10

        elif digito == 4:
            num_letras += 'cuatro-'
            invertido //= 10

        elif digito == 5:
            num_letras += 'cinco-'
            invertido //= 10

        elif digito == 6:
            num_letras += 'seis-'
            invertido //= 10

        elif digito == 7:
            num_letras += 'siete-'
            invertido //= 10

        elif digito == 8:
            num_letras += 'ocho-'
            invertido //= 10

        elif digito == 9:
            num_letras += 'nueve-'
            invertido //= 10

    longitud = length(num_letras)

    num_letras = num_letras[:longitud-1]

    return num_letras



#Ejercicios de taller (por puro amor al arte)

#Ejercicio 2
#Entradas: Un número entero entre 0 y 9
#Salidas: Ese mismo número pero en letras
#Restricciones: El número de entrada debe ser entero y estar dentro del rango establecido
'''Hay una tupla con todos los nombres de los números del 0 al 9 y un contador, mediante un bucle for que recorre la tupla se va verificando hasta que un contador es igual al número ingresado.
El contador coincide con el elemento de la variable del bucle for siempre, por lo que una vez el contador coincida con el número, el elemento de la variable bucle se devuelve.'''

def numLetras(numero):

    numeros_letras = ('cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve')
    contador = 0

    for i in numeros_letras:
        if numero == contador:
            return i
        else:
            contador += 1


#Ejercicio 4
#Entradas: Un número cualquiera.
#Salidas: Ese número dividido entre 7.
#Restricciones: El número debe ser un número real.
'''Toma un número, lo divide entre 7 y devuelve el resultado.'''

def foo(op):
    return op / 7

#Resultados a obtener
#foo(14) = 14/7 = 2
#foo(20 + foo(7)) = (20 + 7 / 7) / 7 = (20 + 1) / 7 = 21 / 7 = 3

#Ejercicio 6
#Entradas: Un número entero que representa una cantidad de dinero
#Salidas: La cantidad de denominaciones que contiene ese dinero 
#Restricciones: El número debe ser entero.
'''Toma la cantidad de dinero y va realizando diversas comprobaciones, cada una resta una determinada denominación a la cantidad de dinero original y añade uno a esa misma denominación y así con todas.'''

def desglose(dinero):
    cantidad100 = 0
    cantidad50 = 0
    cantidad20 = 0
    cantidad10 = 0
    cantidad5 = 0
    cantidad1 = 0

    while dinero >= 100:
        dinero -= 100
        cantidad100 += 1

    while dinero >= 50:
        dinero -= 50
        cantidad50+= 1

    while dinero >= 20:
        dinero -= 20
        cantidad20 += 1

    while dinero >= 10:
        dinero -= 10
        cantidad10 += 1

    while dinero >= 5:
        dinero -= 5
        cantidad5 += 1

    while 0 < dinero < 5:
        dinero -= 1
        cantidad1 += 1

    return (cantidad100, cantidad50, cantidad20, cantidad10, cantidad5, cantidad1)

#Ejercicio 8
#Entradas: 3 números cualquiera
#Salidas: Esos números ordenados de mayor a menor
#Restricciones: Los números deben ser reales
'''Verifica si los valores de a y b están ordenados correctamente, en caso de no estarlo los reasigna entre ellos. Luego verifica si b y c están ordenado y en caso de no estarlo, realiza el mismo
proceso. Finalmente vuelve a verificar a y b y devuelve los números ordenados.'''

def orden(a, b, c):

    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    return a, b, c

#Ejercicio 10
#Entradas: 2 números cualquiera (a y c).
#Salidas: El parametro a que recibe la función elevado al cuadrado más 10.
'''La función genera una función lambda dentro de ella en la que toma el parametro a de la función padre y lo eleva al cuadrado, luego a este se le suma 10 y se devuelve el resultado.'''

def misterio(a, c):
    b = lambda x: a**2 #Se declara una función lambda en la que entra un parametro x y el parametro a de la función padre se eleva al cuadrado. Esto se almacena en una variable de nombre b.
    d = b(c) + 10 #Al resultado de la función lambda se le suma 10 y se almacena una variable d.
    return d #Se devuelve el valor de d.

#Ejercicio 12
#Entradas: El número de horas trabajadas y la tarifa por hora que cobra el trabajador.
#Salidas: El salario de ese trabajador por las horas trabajadas tomando en cuenta las horas extras.
#Restricciones: Los datos deben ser números reales y positivos.
'''Primer se verifica si las horas son mayores a 50 o no, en caso de no serlo se calcula el salario mutiplicando las horas por la tarifa. En caso de ser mayor a 50, se calculan las horas extras, y
la tarifa extra multiplicando la tarifa base por 0.5 y entonces las horas extras son multiplicadas por esa nueva tarifa. Una vez hecho eso, se calcula el salario de las horas normales y se le suma
el salario obtenido de las horas extra.'''

def calcSalario(horas, tarifa):
    salario = 0
    tarifa_extra = 0
    horas_extra = 0

    if horas <= 40:
        salario = horas * tarifa
        return salario
    else:  
        horas_extra = horas - 40
        tarifa_extra = tarifa * 0.5
        salario = ((horas - horas_extra) * tarifa) + (horas_extra * tarifa_extra)
        return salario

#Ejercio 14
#Entradas: 3 números enteros que representan horas, minutos y segundos.
#Salidas: Cuántos minutos quedan para terminar el día
#Restricciones: Los 3 datos de entrada deben ser enteros. Las horas en un rango de 0 a 23, los minutos y segundos en un rango de 0 a 60
'''Primero se calculan los datos de las horas y segundos en minutos y se suman. Posteriormente se la resta de los minutos totales que tiene un día entre los minutos calculados.'''

def faltante(horas, minutos, segundos):
    horas_min = horas * 60
    seg_min = segundos / 60
    min_totales = horas_min + minutos + seg_min

    return 1440 - min_totales

#Ejercicio 16
#Entradas: Un número de exactamente 3 dígitos.
#Salidas: El dígito más significativo del número.
#Restricciones: El número debe ser de 3 dígitos y entero
'''La función primero verifica que el número sea de 3 dígitos, si lo es, procede a realizar una divisón entera entre 100 para obtener el dígito más siginificativo.'''

def significativo(num):
    if num < 100 or num > 999:
        return "Error en numero de entrada"
    else:
        return num // 100

#Ejercicio 18 
#Entradas: Cantidad de años (n), cantidad depositada inicialmente (P) y el porcentaje de interés compuesto aplicado de forma decimal (i)
#Salidas: El dinero acumulado
#Restricciones: Los datos deben pertenecer a los números reales
'''Una vez recibidos los datos, el interés dinero acumulado es calculado mediante una fórmula y devuelto.'''

def interesCompuesto(P, i, n):
    return P * ((1 + i)**n)

#Ejercicio 20
#Entradas: Un número cualquiera
#Salidas: El mismo número pero invertido
#Restricciones: El número debe ser entero
'''Esta función recibe un número y lo va descomponiendo poco y extrayendo los dígitos, cada dígito luego es añadido a una variable llamada invertido en la que la misma variable es multiplicada por
10 y se le añade el último dígito extraído.'''

def invertir(num):
    invertido = 0
    digito = 0

    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num //= 10

    return invertido