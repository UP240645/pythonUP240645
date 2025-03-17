# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1
print(len(set(age)) < len(age))  
#2
"""
la tupla es inmutable lo que significa que no se puede cambiar ni actualizar una vez creadas 
en cambio las listas permiten modificaciones como agregar eliminar o cambiar datos 
los set son los mismos que las listas solo que en este no puede haber datos duplicados
"""
#3
string = 'I am a teacher and I love to inspire and teach people.'
print(len(set(string.split())))