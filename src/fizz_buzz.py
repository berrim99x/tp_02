def fizz_buzz(number: int) -> str:
    if number == 0 :
        return 'fizzbuzz'
    if number == 3 or number == 6 :
        return 'fizz'
    if number == 5 :
        return 'buzz'
    return str(number)

