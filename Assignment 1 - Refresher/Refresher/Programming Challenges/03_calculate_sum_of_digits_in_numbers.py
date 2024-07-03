
def sum_of_digits_in_int(integers: int | str):
    return sum([int(i) for i in str(integers)])
    

num_input = input("Enter a number : ")

print(f"Sum of digits : {sum_of_digits_in_int(num_input)}")

# Output:
'''
Enter a number : 12345
Sum of digits : 15
'''
