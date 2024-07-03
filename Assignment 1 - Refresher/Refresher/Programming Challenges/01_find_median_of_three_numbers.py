
def median(*numbers):
    numbers = sorted(list(numbers))
    no_of_numbers = len(numbers)      
    
    # Odd median
    if no_of_numbers % 3 == 0:
        odd_median_index = round(no_of_numbers*0.5) - 1
        return numbers[odd_median_index]
        
    # Even median
    even_median_index = sum(numbers)/no_of_numbers
    return numbers[even_median_index]


nums_input_str = input("Enter numbers separated by space : ").split()
nums_input_int = [int(i) for i in nums_input_str]

print(f"Median is : {median(*nums_input_int)}")

# Output:
'''
Enter numbers separated by space : 10 5 20
Median is : 10
'''
