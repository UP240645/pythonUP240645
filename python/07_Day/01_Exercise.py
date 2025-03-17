# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
print(len(it_companies))
#2
it_companies.add("Twitter")
print(it_companies)
#3
it_companies.update("Gmail","Mercado libre","Instagram")
#4
it_companies.remove("Twitter")
print(it_companies)
#5
"""
La diferencia es que remove si se equivoca marca error y discard nunca marca error si no encuentra el elemento
"""