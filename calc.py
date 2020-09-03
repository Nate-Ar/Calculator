# Creator: Nathan A
# Description: Simple Calculator
# Creation Date: 8/3/2020
# Update Date: 
while True:
    aos = input('Do you want to add, subtract, multiply, division or quit() $ ')
    # Add
    if aos.lower() == 'add':
        numb1 = input('First Number$ ')
        numb2 = input('Second Number$ ')
        print(int(numb1) + int(numb2))
    # Subtraction
    if aos.lower() == 'subtract':
        numb1 = input('First Number$ ')
        numb2 = input('Second Number$ ')
        print(int(numb1) - int(numb2))
    # Multiply
    if aos.lower() == 'multiply':
        numb1 = input('First Number$ ')
        numb2 = input('Second Number$ ')
        print(int(numb1) * int(numb2))
    # Division
    if aos.lower() == 'division':
        numb1 = input('First Number$ ')
        numb2 = input('Second Number$ ')
        print(int(numb1) / int(numb2))
    if aos.lower() == 'quit()':
        quit()
