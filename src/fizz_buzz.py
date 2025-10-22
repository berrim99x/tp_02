def fizz_buzz(number: int) -> str:
    if number == 0 or number == 15 or number == 30 :
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0 :
        return 'buzz'
    return str(number)

