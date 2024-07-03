# 1
def print_params(a=1, b='stroke', c=True):
    print(a, b, c, '\n')


print_params(b=25)
print_params(c=[1, 2, 3])

# 2
value_list = [143, b'2', 'KarbonAra']
value_dict = {'a': 44, 'b': b'8', 'c': 'Aviasels'}

print_params(*value_list)
print_params(**value_dict)

# 3
value_list_2 = [-44.3j, False]

print_params(*value_list_2, 42)
