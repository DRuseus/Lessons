
calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    str_inf = list()
    str_inf.append(len(string))
    str_inf.append(string.upper())
    str_inf.append(string.lower())
    str_inf = tuple(str_inf)
    count_calls()
    return str_inf


def is_contains(string, list_to_search):
    string = string.lower()
    is_cont = False
    j = len(list_to_search)
    i = 0
    while i in range(j):
        list_to_search[i] = list_to_search[i].lower()
        if list_to_search[i] == string:
            is_cont = True
            i += 1
            break
        else:
            is_cont = False
            i += 1
            continue
    return is_cont


print(string_info('Capibara'))
print(string_info('TetraChokopai'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
