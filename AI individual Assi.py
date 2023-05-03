import tkinter as tk

def count_chars():
    # Get the string entered by the user
    string = entry.get()

    # Create an empty dictionary to hold the character frequency count
    char_frequency = {}

    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in char_frequency:
            char_frequency[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_frequency[char] = 1

    # Create a string to hold the character frequency count
    count_string = ""
    for char, count in char_frequency.items():
        count_string += f"{count} {char}'s, "

    # Remove the last comma and space from the count string
    count_string = count_string[:-2]

    # Create a label to display the character frequency count
    label.config(text=count_string)


# Create the GUI window
window = tk.Tk()
window.title("Character Frequency Counter")

# Create a label and an entry widget for the user to enter a string
tk.Label(window, text="Enter a string:").grid(row=0, column=0)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

# Create a button to count the character frequency
tk.Button(window, text="Count", command=count_chars).grid(row=1, column=0)

# Create a label to display the character frequency count
label = tk.Label(window, text="")
label.grid(row=2, column=0)

# Start the main loop of the GUI
window.mainloop()

