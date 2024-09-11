# Guess The Number Game
import random
number = random.randint(1, 1000)
attempt = 0

while True:
    try:
        input_number = int(input("Enter your guess between 1 - 1000 (Press 0 to exit): "))
        if input_number == 0:
            print("Exiting the game...")
            break;
        elif not 1 <= input_number <= 1000:
            print("Please check the range and try again.")
            attempt += 1

        elif input_number == number:
            print("Yes. You did it on your", attempt, "attempt.")
            break
        elif input_number < number:
            print("Nope. Try something bigger.")
        else:
            print("Nope. Try something smaller.")
    except ValueError:
        print("Invalid input! Try again...")



print("\n \n \n \n")


# Guess the number game with binary search (Auto Playing)
import random
number = random.randint(1, 1000)
attempt = 0
low = 1
high = 1000
print("Guess the number between 1 to 1000: ")

while True:
    input_number = (low + high) // 2
    print("My guess is", input_number)
    attempt += 1

    if input_number == number:
        print("Yes. You did it on your", attempt, "attempts")
        break
    elif input_number > number:
        print("Nope. Try something smaller")
        high = input_number - 1
    else:
        print("Nope. Try something bigger")
        low = input_number + 1



print("\n \n \n \n")


# Prime Number Checker
def is_prime1(n):
    if n < 2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divisible by:", x)
            prime = False
    return prime

while True:
    number =  int(input("Please enter a number (0 to exit): "))
    if number == 0:
        print("Quitted")
        break
    prime = is_prime1(number)
    if prime is True:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")



print("\n \n \n \n")

# Fibonacci or Not

x = 1
y = 1
n = int(input("Enter a number: "))

if n == 1:
    print(f"{n} is a Fibonacci number.")
else:
    fibonacci = 1
    while fibonacci < n:
        fibonacci = x + y
        x = y
        y = fibonacci

    if fibonacci == n:
        print(f"{n} is a Fibonacci number.")
    else:
        print(f"{n} is not a Fibonacci number.")