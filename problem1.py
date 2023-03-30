#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

mainlist = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']

print(f"The current list is {mainlist}")
old = input("Enter the person to kill: ")
new = input("Enter the replacement: ")
mainlist[mainlist.index(old)] = new
print(f"The modified list is {mainlist}")