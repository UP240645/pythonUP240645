#level 3
import random 
def shuffled_list(array):
    return random.sample(array, len(array))


def seven_random():
    arr = []
    length = -1
    while length <= 7:
        num = random.randint(0, 9)
        if num not in arr:
            arr.append(num)
            length = len(arr)
    return arr
