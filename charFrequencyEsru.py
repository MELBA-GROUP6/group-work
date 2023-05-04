
Word_in = input("Enter any word you need!!") 

all_freq = {}
 
for i in Word_in :
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
# printing result
print("Frequency of characters in the words are:\n "
      + str(all_freq))