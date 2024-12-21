integer=int(input("please enter a number"))

if integer%3==0 and integer%5==0:
    print("FizzBuzz")
elif integer%3==0:
    print("Fizz")
elif integer%5==0:
    print("Buzz")