# Input
name = input("Enter your name: ")
print("Welcome Back,", name,"!")


# Input to Ing
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print("SUM of", num1, "and", num2, "is", num1+num2)


# Index
SAARC = ["Bangladesh","Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
print(SAARC)
print(SAARC[1])
print("UK" in SAARC)
print("Bangladesh" in SAARC)
print("UK" not in SAARC)
print("Bangladesh" not in SAARC)


country = input("Enter your country name: ")
if country in SAARC:
    print("Your country", country, "is a SAARC member.")
else:
    print("Your country", country, "is not a SAARC member.")
print("Program Terminated")


mark = int(input("Enter your mark to check your grade:"))
if mark >= 80:
    grade = "A+"
elif mark >= 70:
    grade = "A"
elif mark >= 60:
    grade = "A-"
elif mark >= 50:
    grade = "B"
elif mark >= 40:
    grade = "C"
elif mark >= 33:
    grade = "D"
else:
    grade = "F"
print("You have got", grade, "grade")


# Positive or Negative
number = int(input("Enter a number to check:"))
if number < 0:
    result = "Its Negative"
else:
    result = "Its Positive"
print(result)


# Even or Odd
number = int(input("Enter a number to check:"))
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")


# Find Maximum Number
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2:
    max = number1
    min = number2
else:
    max = number2
    min = number1

if max > number3:
    max = max
    min = number3
else: 
    max = number3
    min = min

print("The maximum number is:", max, "and the minimum number is: ", min)


# Leap Year
# Method 1
year = int(input("Input a year to check leap year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

if year % 400 == 0:
    result = "is a leap year"
elif year % 100 == 0:
    result = "is not a leap year"
elif year % 4 == 0:
    result = "is a leap year"
else:
    result = "is not a leap year"

print(year, result)

# Method 2
if year % 100 != 0 and year % 4 == 0:
    print(year, "is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")