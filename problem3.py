#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""
l = []

print("Enter up to 10 nums for a list. Enter a negative number to end list.")
for i in range(0, 10):
    n = int(input(f"Enter {i + 1}: "))
    if n > -1:
        l.append(n)
    else:
        print(f"List ended with {len(l)} items.")
        l.sort()
        print(l)
print(f"List completed with {len(l)} items.")
l.sort()
f = l[len(l) - 1]
print(f"The largest number was {f}")
