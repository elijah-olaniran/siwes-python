#Fizz Buzz Algorithm
#it takes a number,retuns fizz if its /3
#returns buzz if its /5 and returns fizzbuzz if its /3 and 5
#else returns the number in string

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 ==0:
        return "buzz"
    return str(num)
print(fizzbuzz(10))
print(fizzbuzz(18))
print(fizzbuzz(75))

