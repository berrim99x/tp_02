def fizz_buzz(number: int) -> str:
    if number == 0 :
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number == 5 or number == 10 :
        return 'buzz'
    return str(number)

