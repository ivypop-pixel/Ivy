favorite_foods = ["ramen", "mutton curry", "larb", "pasta", "chipotle"]
print(favorite_foods[1])
print(favorite_foods[-1])
favorite_foods.append("sushi")
#here i forgot the "" entireky for sushi, so it thought it was a function
print(favorite_foods)
favorite_foods.insert(0,"apple")
print(favorite_foods)
favorite_foods.remove("larb")
#     favorite_foods.remove(3), ValueError: list.remove(x): x not in list. Here i did the index not the value
print(favorite_foods)
print(len(favorite_foods))

for food in favorite_foods:
    print(food.upper())
new_list = [favorite_foods[0], favorite_foods[-1]]
print(new_list)
if "potato" in new_list:
    print ("oh! a potato")
else:
    print ("No potato!")
# NameError: name 'potato' is not defined. here i forgot to include the "" for the if part


# ---3.2 Slicing and Striding ---
numbers = list (range(0,21))
def get_first_15(numbers):
    return numbers[:15]
first_15 = get_first_15(numbers)
print(first_15)

def get_every_5th(lst):
    return lst[::5]
every_5th = get_every_5th(first_15)
print(every_5th)

def reverse_and_stride(lst):
     return lst[::-3]
final_list = reverse_and_stride(every_5th)
print(final_list)

# ---Nestsed Lists ---

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

third = numbers[2]
print(third)
print(numbers[1][1])
numbers.append([10,11,12])
print(numbers)

def sum_nested(nested_list):
    total =0
    for row in nested_list:
        for number in row:
            total += number
    return total
sum = sum_nested(numbers)
print(sum)


# def create_grid():


# --DIctionaries ---
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])

ages["Mira"] =100
print(ages["Mira"])
ages["Milana"] = 52
print(ages)

del ages["Mariam"]

for name, age in ages.items():
 print(f"{name} is {age} years old.")
