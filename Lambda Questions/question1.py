'''
Question 1: You have a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. Use the filter function and a lambda function to create a new list that contains only the strings with more than 5 characters.

- Input: ['apple', 'banana', 'cherry', 'date', 'elderberry']
- Expected Output: ['banana', 'cherry', 'elderberry']

'''


input_lst: list[str] = ['apple', 'banana', 'cherry', 'date', 'elderberry']

filtered_lst: list[str] = list(filter(lambda s: len(s) > 5, input_lst))

print(f"Filtered list of more than 5 characters words is : {filtered_lst}")


# Output:
'''
Filtered list of more than 5 characters words is : ['banana', 'cherry', 'elderberry']
'''
