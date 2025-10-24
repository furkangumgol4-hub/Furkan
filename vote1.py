# source code:
age = int(input("enter your age: "))
if age < 0:
    print("age cant be negative.")
elif age < 18:
    print("age you are not eligible to vote.")
else:
    print("you are eligible to vote.")
