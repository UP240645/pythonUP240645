# Level 1
# 1
for i in range(0, 11):
    print(i)

k = 0
while k <= 10:
    print(k)
    k = k+1

# 2
for i in range(10,0):
    print(i)

k = 10
while k >= 0:
    print(k)
    k = k-1

# 3
hash_string = '#'
for i in range(1, 8):
    print(hash_string * i)

# 4
for i in range(1, 9):
    for j in range(1, 9):
        print("#", end=' ')
    print()

# 5
for i in range(0, 11):
    print(i, "x", i, "=", i * i)

# 6
for lang in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(lang)

# 7
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

# 8
for i in range(0, 101):
    if i % 2 != 0:
        print(i)
