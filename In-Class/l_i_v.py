import random

wordbank= ["indentation", "spaces"] 
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# Add a line of code that appends the integer 4 to the list wordbank.

wordbank.append(4)
# print(wordbank)

# Include an input asking for a number between 0 and 20. Save this as the variable num.

num = int(input("Enter a number between 0 and 20: "))

# Use the integer num to slice one of the elements from the list tlgstudents. Save the name you return as the variable student_name.

student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")
