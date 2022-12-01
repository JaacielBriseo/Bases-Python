# def saludar():
#     print('Hola que tal?')


# saludar()


# def saludar_persona(persona='Persona generica'):
#     print(f'Hola que tal {persona}')


def sumar(a, b):
    return a + b


def resta(a, b):
    return a - b


def dividir(a, b):
    return a / b


def multiplicar(a, b):
    return a * b


# print(sumar(5, 5))
# print(resta(5, 5))
# print(dividir(5, 5))
# print(multiplicar(5, 5))
def programa():
    menu = int(input("""[1] Para sumar
[2] Para restar
[3] Para dividir
[4] Para multiplicar
[5] Para salir del programa
    """))

    if menu == 1:
        num1 = int(input('Ingrese el primer numero para sumar: '))
        num2 = int(input('Ingrese el segundo numero para sumar: '))
        resultado = sumar(num1, num2)
        print(f'El resultado de la suma es = {resultado}')
    elif menu == 2:
        num1 = int(input('Ingrese el primer numero para restar: '))
        num2 = int(input('Ingrese el segundo numero para restar: '))
        resultado = resta(num1, num2)
        print(f'El resultado de la resta es = {resultado}')
    elif menu == 3:
        num1 = int(input('Ingrese el primer numero para dividir: '))
        num2 = int(input('Ingrese el segundo numero para dividir: '))
        resultado = dividir(num1, num2)
        print(f'El resultado de la division es = {resultado}')
    elif menu == 4:
        num1 = int(input('Ingrese el primer numero para multiplicar: '))
        num2 = int(input('Ingrese el segundo numero para multiplicar: '))
        resultado = multiplicar(num1, num2)
        print(f'El resultado de la multiplicacion es = {resultado}')
    elif menu == 5:
        print('Saliendo del programa...')
        exit()
    else:
        print('Opcion no valida')
        
while True:
    programa()