def count_characters(string):
    """
    Function to count the frequency of each character in a string.
    """
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Loop until user decides to stop
while True:
    # Take user input for string
    string = input("Enter a string: ")

    # Call the count_characters function to get the frequency count
    char_count = count_characters(string)

    # Print the result
    for char, count in char_count.items():
        print(count, char+"'s")

    # Ask user if they want to continue or stop
    answer = input("Do you want to continue? (y/n): ")
    if answer.lower() == 'n':
        break

print("Program stopped.")