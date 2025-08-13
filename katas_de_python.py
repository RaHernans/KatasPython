# 📘 Proyecto de Katas en Python 
# Descripción: Este archivo contiene la resolución de 41 ejercicios (katas) de lógica en Python,
# con comentarios explicativos en las partes más importantes del código.

# ---------------------------------------------------------------------
# 🧪 Ejercicio 1
# Escribe una función que reciba una cadena de texto como parámetro y devuelva
# un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_letras(texto):
    texto = texto.replace(" ", "") 
    frecuencias = {}
    for letra in texto:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias

print(contar_letras("hola mundo"))  # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

# ---------------------------------------------------------------------
# 🧪 Ejercicio 2
# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

def lista_duplicada(lista):
    return list(map(lambda x: x * 2, lista))


print(lista_duplicada([1, 2, 3, 4]))  # [2, 4, 6, 8]

# 🧪Ejercicio 3
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo
def filtrar_palabras(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]
lista_palabras= ["avión", "ventana", "invierno", "vino", "universo", "evento", "aventura", "vino"]
resultado = filtrar_palabras(lista_palabras, "ven")

print(palabras_que_contienen(["avión", "ventana", "invierno", "vino", "universo", "envento", "aventura"], "ven"))

#🧪Ejercicio 4
# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función 
# map()
def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))
lista1 = [10, 20, 30]
lista2 = [1, 5, 25]
resultado = diferencia_listas(lista1, lista2)
print("Diferencia entre listas:", diferencia_listas([10, 20, 30], [1, 2, 3]))

# 🧪Ejercicicio 5
#  Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
# una tupla que contenga la media y el estado.
def evaluar_nota(lista, nota_aprobado=5):
    if not lista:
        return (0, "suspenso")
    media = sum(lista) / len(lista)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

notas = [4, 6, 7, 5]
resultado = evaluar_nota(notas)
print("Evaluar media:", evaluar_media([4, 6, 5]))

# 🧪Ejercicio 6
# Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial de 5:", factorial(5))


# 🧪Ejercicio 7 
# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función 
#map()
def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))

tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = tuplas_a_strings(tuplas)
print("Lista de tuplas a strings:", tuplas_a_strings([("Hola", "mundo"), ("Python", "es", "genial")]))

# 🧪Ejercicio 8 
#  Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
#indicando si la división fue exitosa o no.
def dividir_numeros():
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        resultado = a / b
        print("División exitosa:", resultado)
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
if __name__ == "__main__":
    dividir_numeros()
      
# 🧪Ejercicio 9 
# Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función 
#filter()

def mascotas_permitidas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))
print("Mascotas permitidas:", mascotas_permitidas(["Perro", "Gato", "Tigre", "Canario"]))
 
# Ejercicio 10 
# Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
#excepción personalizada y maneja el error adecuadamente.
def calcular_promedio(lista):
    if not lista:
        raise ValueError("La lista está vacía. No se puede calcular el promedio.")
    return sum(lista) / len(lista)

try:
    print("Promedio:", calcular_promedio([5, 7, 9]))
except ValueError as e:
    print("Error:", e)


# 🧪Ejercicio 11
# Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
#adecuadamente.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera del rango permitido (0-120).")
        
        print(f"Edad registrada correctamente: {edad} años.")
        return edad

    except ValueError as e:
        print(f"Error: {e}")
        return None
pedir_edad()


# 🧪Ejercicio 12 
# Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función 
def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))
frase = "Python es un lenguaje complicado al principio"
print(longitudes_palabras(frase))


# 🧪Ejercicio 13 
# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def letras_mayus_minus(conjunto):
    unicas = set(conjunto)  # Asegura que no haya letras repetidas
    return list(map(lambda c: (c.upper(), c.lower()), unicas))

caracteres = {'a', 'b', 'C', 'd', 'a', 'D'}
resultado = letras_mayus_minus(caracteres)
print(resultado)

#🧪Ejercicio 14
# Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la 
#función filter()
def palabras_con_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

palabras = ["gato", "perro","golondrina","gallo","pez","jirafa"]
print(palabras_con_letra(palabras, "g"))


#🧪 Ejercicio 15
# Crea una función lambda que  sume 3 a cada número de una lista dada.
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

numeros = [1, 2, 3, 4]
print(sumar_tres(numeros))


#🧪 Ejericio 16
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
#todas las palabras que sean más largas que n. Usa la función filter()
def palabras_mas_largas_que(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

print(palabras_mas_largas_que("La inteligencia artificial es fascinante", 4))
 
# 🧪Ejercicio 17 
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] 
#corresponde al número quinientos setenta y dos [572]. Usa la función reduce()
from functools import reduce

def convertir_a_numero(lista_digitos):
    return reduce(lambda x, y: x * 10 + y, lista_digitos)

print(convertir_a_numero([5, 7, 2]))  # Resultado: 572

 
# 🧪Ejercicio 18 
# Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
#90. Usa la función filter()
estudiantes = [
    {"nombre": "Ana", "edad": 25, "calificacion": 95},
    {"nombre": "Luis", "edad": 29, "calificacion": 85},
    {"nombre": "María", "edad": 32, "calificacion": 90}
]
estudiantes_destacados = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))

print(estudiantes_destacados)
# Resultado: [{'nombre': 'Ana', ...}, {'nombre': 'María', ...}]

# 🧪Ejercicio 19 
# Crea una función lambda que filtre los números impares de una lista dada.
numeros_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

print(numeros_impares([1, 2, 3, 4, 5]))  # Resultado: [1, 3, 5]

# 🧪Ejercicio 20 
# Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
#filter()
solo_enteros = lambda lista: list(filter(lambda x: isinstance(x, int), lista))

print(solo_enteros([1, 'dos', 3, 'cuatro', 5]))  # Resultado: [1, 3, 5]

 
 # 🧪Ejercicio 21 
 # Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo = lambda x: x ** 3

print(cubo(3))  # Resultado: 27

# 🧪Ejercicio 22 
# Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() 
def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

print(producto_total([1, 2, 3, 4]))  # Resultado: 24

# 🧪Ejercicio 23
#Concatena una lista de palabras.Usa la función reduce ().
def concatenar_palabras(lista):
    return reduce(lambda x, y: x + y, lista)

print(concatenar_palabras(["Hola", " ", "mundo"]))  # Resultado: "Hola mundo"

#🧪 Ejercicio 24
#Calcula la diferencia total en los valores de una lista. Usa la función reduce ().
def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

print(diferencia_total([100, 20, 10]))  # Resultado: 70 (100 - 20 - 10)

# 🧪Ejercicio 25
#Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    return len(cadena)

print(contar_caracteres("Python"))  # Resultado: 6

# 🧪Ejercicio 26
# Crea una función lambda que calcule el resto de la división entre dos números dados.
resto_division = lambda a, b: a % b

print(resto_division(10, 3))  # Resultado: 1

# 🧪Ejercicio 27 
#Crea una función que calcule el promedio de una lista de números.
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

print(promedio([10, 20, 30]))  # Resultado: 20.0

# 🧪Ejercicio 28 
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()
    for num in lista:
        if num in vistos:
            return num
        vistos.add(num)
    return None

print(primer_duplicado([1, 3, 4, 2, 3, 5]))  # Resultado: 3
# 🧪Ejercicio 29 
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.
def enmascarar_cadena(cadena):
    if len(cadena) <= 4:
        return cadena
    return '#' * (len(cadena) - 4) + cadena[-4:]

print(enmascarar_cadena("123456789"))  # Resultado: #####6789

# 🧪Ejercicio 30
#Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(son_anagramas("Roma", "Amor"))  # Resultado: True

# 🧪Ejercicio 31
#Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, 
# se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
def buscar_nombre():
    try:
        nombres = input("Introduce nombres separados por coma: ").split(",")
        nombres = [n.strip() for n in nombres]
        buscar = input("Introduce el nombre a buscar: ").strip()
        if buscar in nombres:
            print("Nombre encontrado.")
        else:
            raise ValueError("El nombre no está en la lista.")
    except ValueError as e:
        print("Error:", e)

 

# 🧪Ejercicio 32
#Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, 
# de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
def buscar_puesto(nombre, empleados):
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre.lower():
            return empleado["puesto"]
    return "La persona no trabaja aquí."

empleados = [
    {"nombre": "Laura Martínez", "puesto": "Gerente"},
    {"nombre": "Carlos Pérez", "puesto": "Analista"},
]
print(buscar_puesto("Carlos Pérez", empleados))  # Resultado: Analista

# 🧪Ejercicio 33
#Crea una función lambda que sume elementos correspondientes de dos listas dadas
sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

print(sumar_listas([1, 2, 3], [4, 5, 6]))  # Resultado: [5, 7, 9]

# 🧪Ejercicio 35
#Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
#crecer_tronco , 
#nueva_rama , 
#crecer_ramas , 
#quitar_rama e 
#info_arbol.
# El objetivo es implementar estos métodos para manipular la estructura del árbol.
#Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
#Caso de uso:
 #1. Crear un árbol.
 #2. Hacer crecer el tronco del árbol una unidad.
 #3. Añadir una nueva rama al árbol.
 #4. Hacer crecer todas las ramas del árbol una unidad.
 #5. Añadir dos nuevas ramas al árbol.
 #6. Retirar la rama situada en la posición 2.
 #7. Obtener información sobre el árbol.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "Longitud del tronco": self.tronco,
            "Número de ramas": len(self.ramas),
            "Longitudes de ramas": self.ramas
        }
    
#Caso de uso:
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
print(arbol.info_arbol())
# Resultado:
# {'Longitud del tronco': 2, 'Número de ramas': 2, 'Longitudes de ramas': [2, 1]}

# 🧪Ejercicio 35 
#No aparece

#🧪 Ejercicio 36
# Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero,
#  transferir dinero desde otro usuario y agregar dinero al saldo.
#Código a seguir:
 #1.Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente medianteTrue y False.
 #2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
 #3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
  #Lanzará un error en caso de no poder hacerse. 
 #4.Implementar el método gregar_dinero para agregar dinero al saldo del usuario.
 
 #Caso de uso:
  #1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
  #2. Agregar 20 unidades de saldo de "Bob".
  #3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
  #4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError("El usuario no tiene suficiente saldo.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# Caso de uso:
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)               # Bob ahora tiene 70
alicia.transferir_dinero(bob, 80)    # Bob transfiere 80 a Alicia
alicia.retirar_dinero(50)            # Alicia retira 50

print("Alicia - Saldo:", alicia.saldo)  # Resultado: 130
print("Bob - Saldo:", bob.saldo)        # Resultado: -10 (si no se valida negativo)
 
#🧪 Ejercicio 37
# Crea una función llamada procesar_texto que procesa un texto según la opción especificada:  contar_palabras, reemplazar_palabras , 
#eliminar palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar texto. 

#Codigo a seguir: 
#1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#2. Crear una función reemplazar palabras para empezar una palabra original del texto por una palabra nueva. Tiene que devolver el texto con 
# el reemplazo de palabras.
#3. Crear una función eliminar palabras  para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
#4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") 
# y un número de argumentos variable según la opción indicada.

# Caso de uso: 
# Comprueba el funcionamiento completo de la función procesar_texto

# 1. Función para contar cuántas veces aparece cada palabra.
def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.strip(".,!?").lower() 
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

# 2. Función para reemplazar una palabra por otra.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# 3. Función para eliminar una palabra del texto.
def eliminar_palabras(texto, palabra_a_eliminar):
    palabras = texto.split()
    resultado = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return " ".join(resultado)

# 4. Función principal que selecciona la operación a realizar.
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabras(texto, args[0])
    else:
        return "Opción no válida o argumentos incorrectos."
    
    
texto_ejemplo = "Hola mundo hola universo. Hola mundo."

print("contar:", procesar_texto(texto_ejemplo, "contar"))
# Resultado: {'hola': 3, 'mundo': 2, 'universo': 1}

print("reemplazar:", procesar_texto(texto_ejemplo, "reemplazar", "mundo", "planeta"))
# Resultado: Hola planeta hola universo. Hola planeta.

print("eliminar:", procesar_texto(texto_ejemplo, "eliminar", "hola"))
# Resultado: mundo universo. mundo.

# 🧪Ejercicio 38
# Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_del_dia():
    try:
        hora = int(input("Introduce la hora (0-23): "))
        if 6 <= hora < 12:
            print("Es de mañana.")
        elif 12 <= hora < 18:
            print("Es de tarde.")
        elif 0 <= hora < 6 or 18 <= hora <= 23:
            print("Es de noche.")
        else:
            print("Hora no válida.")
    except ValueError:
        print("Por favor, introduce un número válido.")

# 🧪Ejercicio 39
# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
#Las reglas de calificación son:
# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Nota no válida"

print(calificacion_texto(85))  # Resultado: Muy bien

# 🧪Ejercicio 40 
# Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triángulo") y 
# datos (una tupla con los datos necesarios para calcular el área de la figura).
def area_figura(figura, datos):
    if figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    elif figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio, = datos
        return 3.1416 * radio**2
    else:
        return "Figura no válida"
print("Triángulo:", area_figura("triangulo", (5, 3)))    # Resultado: 7.5
print("Rectángulo:", area_figura("rectangulo", (4, 6)))  # Resultado: 24
print("Círculo:", area_figura("circulo", (2,)))          # Resultado: 12.5664

# 🧪Ejercicio 41
# Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. 
# El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.
def calcular_descuento():
    try:
        precio = float(input("Precio original: "))
        tiene_cupon = input("¿Tienes cupón de descuento? (sí/no): ").strip().lower()

        if tiene_cupon == "sí":
            valor_cupon = float(input("¿Cuánto vale el cupón?: "))
            if valor_cupon > 0:
                precio -= valor_cupon
        print("Precio final:", precio)
    except ValueError:
        print("Por favor, introduce valores válidos.")







