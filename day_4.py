# Function
# def add(n1, n2): # Function starts here
#     return n1 + n2 # Function ends here

# number1 = 4
# number2 = 6
# result = add(number1, number2) # Calling the function
# print(result)

# print(add(20, 50))


# def myfnc(x): # Function starts here
#     print("inside myfnc", x)
#     x = 10
#     print("inside myfnc", x) # Function ends here

# x = 20
# myfnc(x) # Calling the function
# print(x) 


# def newFunc(x, y=10, z=0):
#     print("x = ", x, "", "y = ", y, "", "z = ", z)

# x = 5
# y = 6
# z = 7
# newFunc(x, y, z)
# newFunc(x, y)
# newFunc(x)


# def addNum(numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     return result
    
# result = addNum([1, 5, 6, 10])
# print(result)


# list1 = [1, 2, 3, 4]
# list2 = list1

# print(list1)
# print(list2)

# list2[0] = 100

# print(list2)
# print(list1)


# li = [10, 20, 30]
# result = sum(li)
# print(result)


def average():
    count = int(input("How many numbers do you want to input? "))
    total = 0
    
    for i in range(count):
        number = int(input(f"Enter number {i+1}: "))
        total += number
    average = total / count
    return average

result = average()
print("The average is:", result)