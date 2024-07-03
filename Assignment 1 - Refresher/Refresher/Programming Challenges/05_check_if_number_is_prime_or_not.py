
def is_prime(number):
    for i in range(2, round(number**0.5)):
        if number % i == 0:
            return False

    return True


num_input = int(input("Enter a number : "))

print(f"{num_input} is {"" if is_prime(num_input) else "not "}a prime number.")

# Output:
'''
Enter a number : 29
29 is a prime number.
'''
