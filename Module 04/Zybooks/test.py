'''
user_values = [2, 5, 8]
user_values[0] = user_values[0] + 1

print(user_values)


user_values = [1, 5, 7]
user_values[2] = user_values[2] + 1
user_values[0] = user_values[0] + 2

print(user_values)


user_values = [2, 6, 9]
user_values[2] = user_values[0]

print(user_values)
''''''
user_values = [3, 5, 7]
user_values[2] = user_values[1]
user_values[1] = user_values[0]

print(user_values)
'''
'''
my_list = [13, 14, 15, 16, 17]
new_list = my_list[-5:-2]
print(new_list)
''''''
user_values = [1, 5, 8, 4]

max_value = user_values[0]
for i in range(len(user_values)):
  if user_values[i] >= max_value:
    max_value = user_values[i]
    print(max_value)
    '''''''
nums = [10, 20, 30, 40, 50]

for pos in range(len(nums)):
    tmp = nums[pos] / 2
    if (tmp % 2) == 0:
        nums[pos] = tmp    
''''''
my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number - 4 for number in my_list if (number <= 0) and (number % 2 == 0) ]
print(new_list)
''''''
airport_codes = {
    "London": "LHR",
    "Chicago": "ORD",
    "Osaka": "KIX"
}

print(airport_codes["Chicago"])
airport_codes["Chicago"] = "MDW"
print(airport_codes["London"])
print(airport_codes["Chicago"])
'''
provincial_capitals = {
    "Manitoba": "Winnipeg",
    "Ontario": "Toronto",
    "Nunavut": "Iqaluit",
    "Yukon": "Whitehorse"
}

provincial_capitals = {
    "Yukon": "Whitehorse",
    "Manitoba": "Winnipeg",
    "Ontario": "Toronto",
    "Alberta": "Edmonton"
}
'''
province_name = input()
while province_name != "exit":
    if province_name in provincial_capitals:
        print(provincial_capitals[province_name])
    else:
        print("x")
    province_name = input()
'''
'''
airport_codes = {
    "Cincinnati": "CVG",
    "Paris": "CDG",
    "Seattle": "SEA",
    "Chicago": "ORD",
    "Tokyo": "NRT"
}

new_airport_codes = {
    "Minneapolis": "MSP",
    "Chicago": "MDW",
    "San Francisco": "SFO"
}

print(airport_codes.get("Minneapolis", "na"))
print(airport_codes.get("Chicago", "na"))
airport_codes.update(new_airport_codes)
print(airport_codes.get("Minneapolis", "na"))
print(airport_codes.get("Chicago", "na"))
'''
'''
# Read input numbers and convert them to a list of floats
numbers = list(map(float, input().split()))

# Calculate max and average
max_val = max(numbers)
avg_val = sum(numbers) / len(numbers)

# Output with two decimal places
print(f"{max_val:.2f} {avg_val:.2f}")
'''
'''
cities = {
    'London': 982,
    'Austin': 438,
    'Toronto': 5259,
    'Montreal': 3435,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)
'''
'''
for i in range(0, -5, -1):
    print(i, end=" ")
'''
'''
stop = int(input())

for a in range(5):
    result = 0
    
    for b in range(4):
        result += b
    
    result += a
    
    print(result)
    
    if result > stop:
        break
    '''
'''
threshold = int(input())

for a in range(0, 4):
    print(a + 1, end=": ")

    for b in range(0, 1):
        if a > threshold:
            print("_,", end="")
            continue

        print(b, end=",")

    print()
'''
i = 1
while i < 19:
    j = 5
    while j <= 7:
        print(f"{i}{j}")
        j = j + 4
    i = i + 18