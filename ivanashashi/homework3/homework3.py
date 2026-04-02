
# i didnt have time so for the things that have errors i made them into comments so i could print
def say_goodbye(name):
	print ("Bye,", name)
def area_circle(radius):
	area = 3.14 * radius ** 2
	print ("the area is", area)
#4
def subtract(a, b):
	return a- b
def multiply(a, b):
	return a * b
def divide (a, b):
	return a/b

#chp 5

def temp_list(temp):
	return (min(temp), max(temp))
"readings =15, 14, 17, 20, 23, 28, 20]"
# print (min(temp(readongs))

#weekend
def is_weekend(day):
	if day == 6 or day == 7:
		return True
	else: 
		return False
#5.3
def fuel_eff(distance, fuel):
	return distance/fuel
#5.4
def encrypt(interger):
	last_digit = int % 10
	left = int// 10
	return (last_digit + left)
#-----6---

# def power(x,y):
# result = 1
# for i in range(y):
# 	result = result*x
# return result


#.1
# def find_min(value):
	# min = value[0]
	# for num in value:
		# if num <min:
		# min = num
	# return mim

#.2
# def while_min(numbers):
# 	min = numbers[0]
# 	i = 0
# 	while i <len(numbers):
# 	if numbers[i]< min
# 	min = numbers[1]
# 	i += 1
# retrun min

# def while_max(numbers):

#         max= numbers[0] 

#         i = 0

#         while i <len(numbers):

#         if numbers[i]>max

#         max = numbers[1]

#         i += 1

# retrun max


# def sum_digits(numbers)
# total = 0
# 	for digit in str(number):
# 	total += int(digit)
# return total

#         if numbers[i]>max
   
#         max = numbers[1]

#         i += 1
        
# retrun max   
def sum_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

result = sum_digits(2468)
print(result)



# dfavorite function = sum digits