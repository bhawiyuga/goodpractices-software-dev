import pytest

def fizz_buzz(input):
    if input <= 0:
        raise ValueError("Input must be a positive integer")
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
    
    

def test_fizz_buzz_multiples_of_three_and_five():
    # Testing for multiples of both 3 and 5
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(30) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"

def test_fizz_buzz_multiples_of_three():
    # Testing for multiples of 3
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(6) == "Fizz"
    assert fizz_buzz(9) == "Fizz"

def test_fizz_buzz_multiples_of_five():
    # Testing for multiples of 5
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(10) == "Buzz"
    assert fizz_buzz(20) == "Buzz"

def test_fizz_buzz_other_numbers():
    # Testing for numbers that are not multiples of 3 or 5
    assert fizz_buzz(1) == 1
    assert fizz_buzz(2) == 2
    assert fizz_buzz(7) == 7

def test_fizz_buzz_zero_or_negative_numbers():
    # Testing with zero or negative numbers
    with pytest.raises(ValueError):
        fizz_buzz(0)
    with pytest.raises(ValueError):
        fizz_buzz(-1)



