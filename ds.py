

# 🧩 1. List → ordered, changeable, allows duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")   # add
fruits[1] = "mango"       # modify
print(fruits)             # ['apple', 'mango', 'cherry', 'orange']
print(fruits[0])          # access first item
print(len(fruits))        # length



colors = ("red", "green", "blue")
print(colors[1])          # 'green'
print(len(colors))
# colors[1] = "yellow" ❌ (Error — tuples can’t be changed)


numbers = {1, 2, 3, 3, 4}
numbers.add(5)
print(numbers)            # {1, 2, 3, 4, 5}
numbers.remove(2)
print(3 in numbers)       # True


person = {"name": "Amira", "age": 25, "city": "Cairo"}
print(person["name"])     # Amira
person["age"] = 26        # update
person["email"] = "amira@example.com"  # add new
print(person.keys())      # dict_keys(['name', 'age', 'city', 'email'])

