
def is_even(number):
    return number % 2 == 0


number = int(input("Enter a number : "))

is_odd = "even" if is_even(number=number) else "odd"

print(f"{number} is {is_odd}")

# Output:
'''
Enter a number : 7
7 is odd
'''
