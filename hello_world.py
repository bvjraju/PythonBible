# Ask user fro Name

name = input ("What is your name? : ")

# Ask user for their age

age = input("what is your age?:  ")

# Ask user for city

city = input(" which city do you live in ?:  ")

# Ask user what they enjoy

hobby = input(" What do you enjoy doing ?:  ")

# Create output text

text =  "My name is {}. I am {} years old. I lives in {}. and i love {}."

output = text.format(name,age,city,hobby)

# Print output to screen

print(output)
