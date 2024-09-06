#Data Structure 
#List

# Append Method
saarc = ["Bangladesh","Afghanistan", "Bhutan", "Nepal", "India", "Pakistan"]
print(saarc, "(Saarc)")

saarc.append("Sri Lanka")
print(saarc, "(Sri Lanka appended)")

# Insert Method
fruits = ["mango", "banana", "lichi", "coconut"]
fruits.insert(0, "jackfruit")
fruits.insert(3, "orange")
print(fruits, "(jackfruit and orange added)")

x_list = []
for x in range(10):
    x_list.append(x+1)
print(x_list)

# Remove Method
fruits.remove("mango")
print(fruits, "(mango removed)")

item = "apple"

if item in fruits:
    fruits.remove(item)
else:
    print(item, "is not in fruits list.")

# Sort Method
fruits.sort()
print(fruits, "(Shorted)")

# Reverse Method
fruits.reverse()
print(fruits, "(Reversed Shorted)")

# Pop Method
pop_item = fruits.pop()
print(fruits, "(",pop_item, "item popped)")

pop_item = fruits.pop(2)
print(fruits, "(",pop_item, "item popped by index)")

# Extend Method
new_item = ["apple"]
add_item = fruits.extend(new_item)
print(fruits)


# List Comprehensions
# Ex - 1
li = [1,2,3,4,5]
li2 = []
for item in li:
    li2.append(item*2)
print(li2, "(Normal Code)")

new_li = [2 * item for item in li]
print(new_li, "(Comprehensions)")

# Ex - 2
li = [1, 2, 3, 4, 5, 6]
new_li = []
for x in li:
    if x % 2 == 0:
        new_li.append(x)
print(new_li, "(Normal Code)")

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers, "(Comprehensions)")