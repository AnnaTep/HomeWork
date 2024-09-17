def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(stroka):
    count_calls()
    st = (len(stroka), stroka.lower(), stroka.upper())
    return st


def is_contains(string, list_to_search):
    count_calls()
    st = ()
    z = False
    for i in list_to_search:
        i = i.upper()
        string = string.upper()
        if i == string:
            z = i
        else:
            z = 'Нет совпадений'
    return z


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
