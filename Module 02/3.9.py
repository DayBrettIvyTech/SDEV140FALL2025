'''

#  import math

# x = math.fabs(3.1)
# print(x)

# import math

# x = math.pow(3.0, 2.0)
# print(x)

# import math

# x = math.fabs(-8.0 + 1.0)
# print(x)

# import math

# x = math.pow(5.0, math.sqrt(4.0))
# print(x)

# print("Sara\\\nJoe\\nBeth\nAlex")	
# print(r"The escape sequence for single quote is \'")

# user_num = int(input())
# div_num = int(input())

# Perform floor division three times
# result1 = user_num // div_num
# result2 = result1 // div_num
# result3 = result2 // div_num

# Print results on one line
print(result1, result2, result3)



miles_per_gallon = float(input())
dollars_per_gallon = float(input())

# Calculate costs here:
cost_20 = (20 / miles_per_gallon) * dollars_per_gallon
cost_75 = (75 / miles_per_gallon) * dollars_per_gallon
cost_500 = (500 / miles_per_gallon) * dollars_per_gallon

# Print with two decimals!
print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")

'''
'''
age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())

calories = ((age * 0.2757 + weight * 0.03295 + heart_rate * 1.0781 - 75.4991) * time) / 8.368

print(f"Calories: {calories:.2f} calories")

'''

import math

x = float(input())
y = float(input())
z = float(input())

# Assign Values and do Mathy Bits here
value1 = math.pow(x, z)             
value2 = math.pow(x, math.pow(y, z))  
value3 = abs(x - y)                 
value4 = math.sqrt(value1)          

# Output to 2 dec. places.
print(f"{value1:.2f} {value2:.2f} {value3:.2f} {value4:.2f}")
