
def largest_num(number_list: list):
    largest = sorted(list(number_list), reverse=True)[0]
    return largest


nums_input_str = input("Enter numbers separated by space : ").split()
nums_input_int = [int(i) for i in nums_input_str]

print(f"The largest number is: {largest_num(nums_input_int)}")

# Output:
'''
Enter numbers separated by space : 10 25 5
The largest number is: 25
'''
