#punto 1
age = int(18)
#punto 2 
height = 1.78
#punto 3
comp = 8j
print("Tu edad es:",age)
print("Tu altura es:",height)
print("El numero complejo es:",comp)
#punto4
b = int(input('Base = '))
h = int(input('Altura = '))
print('La Area es = ', 0.5*b*h)
#punto 5
lado_a = int(input('Lado a = '))
lado_b = int(input('Lado b = '))
lado_c = int(input('Lado c = '))
perimetro = lado_a + lado_b + lado_c
print('El perimetro es:', perimetro)
#punto 6
largo = int(input('largo = '))
ancho = int(input('ancho = '))
area_rec, perimetro_rec = ancho*largo, 2*(largo + ancho)
print('El area es:', area_rec, 'El perimetro es:', perimetro_rec)
#punto 7
radio = int(input('Ingresa el radio= '))
pi = 3.14
area_circ, circum = pi*radio**2, 2*pi*radio
print('El area es:', area_circ, 'La cirunferencia es:', circum)
#punto 8
x = int(input('x= '))
pendiente = (2*x)-2
print(pendiente)
#punto 9
pendiente1 = (10-2)/(6-2)
print(pendiente1)
#punto 10
x = int(input('x= '))
y = (x**2)+(6*x)+9
print(y)
#punto 11
def calcular_y(x):
    return x**2 + 6*x + 9

# Probar diferentes valores de x
for x in range(-10, 11):  # Probar valores de x entre -10 y 10
    y = calcular_y(x)
    print(f"Para x = {x}, y = {y}")
    
    if y == 0:
        print(f"El valor de x que hace que y = 0 es: {x}")
        break  # Detener el ciclo cuando encontramos el valor de x que hace y = 0
#punto 12
print(len('python') < len('dragon'))
#punto 13
print('on' in 'python' and 'on' in 'dragon')
#punto 14
print('jargon' in 'i hope this course is not full of jargon')
#punto 15
print('on' not in 'python' and 'on' not in 'dragon')
print(len('python'))
#punto 16
print(float(len('python')))
print(str(len('python')))
#punto 17
num = int(input ('Ingrese cualquier numero: ')) 
if((num % 2) == 0): print('even') 
else: print('El número proporcionado es impar')
#punto 18
print(7//3 == 2.7)
#punto 19
print('10' == 10)
#punto 20
print(9.8 == 10)
#punto 21
hrs = int(input('Horas: '))
tasa = int(input('tasa: '))
pago = hrs * tasa 
print('pago: ',pago)
#punto 22
años = int(input('Numeros de años: '))
segundos = años*31,536,000 
print('Has vivido por: ', segundos)
#punto 23
for i in range(1,6):
    print(f'{i} {i**0} {i**2} {i**3}')