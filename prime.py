"""
prime.py -- Write the application code here
By Chris Lilley October 3 2023
"""
def generate_prime_factors(num):
    """
    Checks if num is an int and will raise ValueError
    """
    if not isinstance(num, int):
        raise ValueError("Enter only integers")


    # returns empty string for 1
    if num == 1:
        return

    while num % 2 == 0:
        yield 2
        num //= 2

    x = 3
    while x * x <= num:
        while num % x == 0:
            yield x
            num //= x
        x += 2

    if num > 2:
        yield num
