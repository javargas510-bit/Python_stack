#1
for i in range(1, 10, 1):
    print(i)
#Predit prints numbers 1-9
print("\n")

#2
#prints 1 , 4 , 7
for t in range(1, 10, 3):
    print(t)
print("\n")

#3 
#prints 0-4
for y in range(5):
    if y < 5:
        print(y)
    elif y == 3:
        print("y is 3")
print("\n")

#4 prints 20 then decrements by 3
for j in range(20, 1, -3):
    print(j)
print("\n")

#5 
#prints all the cities in the array
cities = ["London", "Paris", "Tokyo"]
for city in cities:
    print(city)
print("\n")

#6
numbers = [7, 13, 8, 42]
for x in range(0, len(numbers)):
    print("index:",x,"value:",numbers[x])
if numbers[len(numbers) - 1] == 42:
    print("The answer to life, the universe, and everything.")
print("\n")

#7
for num in range(10):
    if num % 2 == 0:
        print("Hello")
    elif num % 4 == 0:
        print("World")
    else:
        print(num)
print("\n")

#8
for num in range(10):
    if num % 4 == 0:
        print("Hello")
    elif num % 2 == 0:
        print("World")
    else:
        print(num)
print("\n")

#9
pet_info = {
    'name': "Fido",
    'age': 4,
    'trick': "rolls over"
    }
for key in pet_info:
    print(key)
    print(pet_info[key])

print("\n")

#10
things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)
