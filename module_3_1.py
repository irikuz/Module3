calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(str):
    count_calls()
    tuple = (len(str), str.upper(), str.lower())
    return (tuple)


def is_contains(str, list):
    count_calls()
    str = str.lower()
    list = [s.lower() for s in list]
    if str in list:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
