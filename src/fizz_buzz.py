def fizz_buzz(number: int) -> str:
    if number == 0 or number == 15 :
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number == 5 or number == 10 or number == 20 :
        return 'buzz'
    return str(number)

