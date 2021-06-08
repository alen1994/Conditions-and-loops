number = int(input("Hello User! Enter a number between 1 and 100: "))

print("The number is: " +  str(number))

for number in range(1, number+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)

