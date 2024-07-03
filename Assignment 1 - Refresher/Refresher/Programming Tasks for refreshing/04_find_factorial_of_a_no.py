
# 5x4x3x2x1 = 120

def factorial(number: int):
    if number == 1 or number == 0:
        return 1
    
    fac_num = number*(number-1)
    
    while (number-2) > 1:

        fac_num *= (number-2)

        number -= 1

    return fac_num


num_input = int(input("Enter a number : "))

print(f"Factorial of {num_input} is {factorial(num_input)}")

# Output:
'''
Enter a number : 5
Factorial of 5 is 120
'''
