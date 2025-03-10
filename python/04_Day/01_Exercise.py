# 1
print("Thirty" + "Days" + "Of" + "Python")
#2
print('Codificación' + 'Para' + 'Todos')
#3
empresa= "codificacion para todos"
#4
print(empresa)
#5
print(len(empresa))
#6
print(empresa.upper())
#7
print(empresa.lower())
#8
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())
#9
print(empresa[12:21 ])
#10
print(empresa.index("codificacion"))
print(empresa.find("codificacion"))
#11
print(empresa.replace("codificacion","python"))
#12
print("phytonparatodos".replace("todos","todo"))
#13
print(empresa.split(","))
#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))
#15
print(empresa[0])
#16
print(len(empresa)-1)
#17
print(empresa[10])
#18
palabras = "Python para todos".split()
print(palabras[0][0] + palabras[1][0] + palabras[2][0])
#19
palabras = 'Codificacion para todos'.split()
print(palabras[0][0] + palabras[1][0] + palabras[2][0])
#20
print("Codificacion Para Todos".index('C'))

# 21
print("Codificacion Para Todos".index('P'))

# 22
print("Codificacion Para Todas las Personas".rfind('l'))

# 23
print('No puedes terminar una oración con porque porque porque es una conjunción'.find('porque'))

# 24
print('No puedes terminar una oración con porque porque porque es una conjunción'.rfind ('porque'))
# 25
print('No puedes terminar una oración con porque porque porque es una conjunción'.replace('porque porque porque', ''))
# 26
print('No puedes terminar una oración con porque porque porque es una conjunción'.find('porque'))
#27 Es lo mismo que el punto 25
#28
print('codificacion para todos'.startswith('Codificacion'))

# 29
print('Codificacion para todos'.endswith('codificacion'))

# 30
print('    codificacion para todos    '.rstrip().lstrip())

# 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32
print('-'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
print('Name\tAge\tCountry\tCity\nRishabh\t250\tFinland\tHelsinki')
# 35
print('radio =', 10)
print('area =', 3.14, '* radio **', 2)
print('el area de un circulo con radio de ', 10, 'es', 314, 'metros cuadrados.')
# 36
print('8 + 6 = 14')
print('8 - 6 = 2')
print('8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')