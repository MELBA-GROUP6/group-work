string = input("Enter a string: ")
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency count:")
for char, count in frequency.items():
    print(char, "-", count)
