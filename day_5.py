# String
# Length of a String
country = "Bangladesh"
print (len(country))

# Indexing 
# index starts with 0 and the last value of a string is (len - 1)
print (country[0])
print (country[6])

# Show index with for loop
for c in country:
    print(c)

# We can add two Strings
country = "I Love " + "Bangladesh"
print(country)

# We can search in String 
print(country.find("bangla")) # Case Sensitive; (-1) = not founded
print(country.find("Bangla"))

# We can change anything in String
newCountry = country.replace("Bangladesh", "Bangladesh 2.0") # Case Sensitive
print(newCountry)

# How to remove space from start, end, both side
country = " Bangladesh "
print(country)

lstrip = country.lstrip()
print(lstrip)

rstrip = country.rstrip()
print(rstrip)

strip = country.strip()
print(strip)

# Case Changing
country = "Bangladesh"
uppercase = country.upper()

country = uppercase
lowercase = country.lower()

country = lowercase
capitalize = country.capitalize()

print(uppercase, lowercase, capitalize)


# Split Strings
string = "I love Bangladesh very much"
splitted = string.split()

for word in splitted:
    print(word)

# Count method
print(string.count("e"))

# startswith and endswith method
while True:
    name = input("Insert Your Name. Please starts with Mr, Mrs, Miss: ").strip().capitalize()
    email = input("Insert your gmail: ").strip().lower()
    username = email[:-10] # Remove '@gmail.com' which has 10 characters

    if email.endswith("@gmail.com"):
        if name.startswith("Mrs"):
            print("Welcome Madam, \nYour username is", username) 
            break
        elif name.startswith("Mr"):
            print("Welcome Sir, \nYour username is", username)
            break
        elif name.startswith("Miss"):
            print("Welcome Miss \nYour username is", username)
            break
        else:
            print("Please start with Mr, Mrs, Miss: ")
            
    else:
        print("Please use gmail only: ")