# String Splitting / Splicing Tutorial Lesson:

words = "Hello World Welcome to my planet" # This is a collection of "something".

print(words[0]) # This will print the first character - H.

for x in words: # This will iterate through each term in words and then print it.
  print(x)

words[0:1:1] # words[<start><up-to><step>]

print(words[6:]) # This will give you the rest of the string after Hello.

print(words[0:5]) # This will give you Hello.

print(words[ : :2]) # Every two characters, it will print it.

print(words[ : :-1]) # This will reverse the order.

print(words[-6:]) # This will count from the end of the string.

print(len(words)) # This will count the number of characters in the variable "words"

print(words.split(" ")) # This will print each term in words seperately.

splitted_words = words.split(" ") # Appends the split words to the variable splitted_words

print(splitted_words) # This will then print that variable

print(len(splitted_words)) # counts the number of characters in the variable "splitted_words"

if "World" in splitted_words: # It will look for the world World in splitted_words, if true it will print
  print("It's in there", "World")
  
for x in splitted_words: # For each term that is in splitted_words, it will be printed.
  print(x)

palindrome_words = "Racecar"

palidrome_lowercase_words = palindrome_words.lower()

print(palidrome_lowercase_words) # Check if it is in lowercase

items_in_list = len(palidrome_lowercase_words) # Count the number of items in the lowercase words version

if palidrome_lowercase_words[0] == palidrome_lowercase_words[(items_in_list)-1]: # Easy Mode
  print("It is a palidrome") 

left_middle_item_in_list = (len(palidrome_lowercase_words) / 2) -1
right_middle_item_in_list = (len(palidrome_lowercase_words) / 2) +1

if left_middle_item_in_list == right_middle_item_in_list:
  print("It is a palidrome")
