# For Loop
result = 0
for i in range(51):
    result = result + i
print(result)


# Finding max number using for loop
num = [5, 6, 65, 48, 326]
maxNumber = num[0]
for i in num:
    if i > maxNumber:
        maxNumber = i
print(maxNumber)


result = 0
for num in range(101):
    if num % 5 == 0:
        print(num);
        result += num
print("Sum is:", result)


result = 0
for num in range(5, 101, 5):
    print(num)
    result += num
print("Sum is: ", result)


# While Loop
# Multiplication Table
n = int(input("Please input a positive number: "))
while n <= 0:
    n = int(input("The number must be a positive number: "))

x = 1
while x <= 10:
    print(n,"x",x,"=",x*n)
    x += 1

# Nested While Loop
i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(i,"x",j,"=",i*j)
        j += 1
    print("")
    i += 1


# Nested For Loop
for x in range(1, 6):
    for y in range(x):
        print(x, end="")
    print("")



# Add or Sub two values
terminate = False
while not terminate:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    while True:
        operation = input("Type add/sub to calculate and quit to exit: ").lower()

        if operation == "quit" or operation == "exit":
            terminate = True
            break

        if operation not in ["add", "sub"]:
            print("Invalid value, Retype new value")
            continue

        if operation == "add":
            print("The result is:", num1 + num2)
            break

        if operation == "sub":
            print("The result is:", num1 - num2)
            break
    terminate = True
    