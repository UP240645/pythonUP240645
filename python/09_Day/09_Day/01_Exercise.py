# Level 1
# 1
age = int(input('ingrese su edad: '))
if age >= 18:
    print("tiene edad suficiente para conducir.")
else:
    print("tienes que esperar", 18 - age, "años.")

# 2
my_age = 18

if age == my_age:
    print("nosotros somos de la misma edad")
elif age > my_age:
    print("eres", age - my_age, "años mayor que yo")
else:
    print("soy", my_age - age, "años mayor que tu")

# 3
a = int(input("Enter number: "))
b = int(input("Enter number: "))
if a > b:
    print(a, "es mayor que", b)
elif a < b:
    print(a, "es menor que", b)
else:
    print("ambos numeros son iguales")