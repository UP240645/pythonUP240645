# Level 3

# 1
def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True


# 2
def checK_list(test_list):
    return len(set(test_list)) == len(test_list)


# 3
def homogeneous_type(seq):
    iseq = iter(seq)
    first_type = type(next(iseq))
    return first_type if all((type(x) is first_type) for x in iseq) else False


def isVar(test):
    return re.match(r"[_a-z]\w*$", test, flags=re.I)


# noinspection DuplicatedCode
list_data = countries_data.data
total_languages_initial = []
for i in list_data:
    total_languages_initial.extend(i["languages"])
print("Languages = ", len(set(total_languages_initial)))
counts = {}
for i in total_languages_initial:
    counts[i] = counts.get(i, 0) + 1


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


counts = sort_dict_by_value(counts, True)
for i in list(counts.items())[:20]:
    print(i)
populations = {}
for i in list_data:
    populations[i["name"]] = i["population"]
populations = sort_dict_by_value(populations, True)
for i in list(populations.items())[:20]:
    print(i)