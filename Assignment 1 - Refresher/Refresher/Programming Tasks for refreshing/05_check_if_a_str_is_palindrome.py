
'''
Palindrome: If we reverse a word or a sentece it will be same
e.g:
Original -> wow
Reversed -> wow
wow is palindrome
'''

def is_palindrome(string: str):
    if not string:
        return "It is a empty string"
    
    reversed_str = string[::-1]

    if string == reversed_str:
        return "Palindrome"
        
    return "not Palindrome"


str_input = input("Enter a string : ")

print(f"{str_input} is {is_palindrome(str_input)}")

# Output:
'''
Enter a string : wow
wow is Palindrome
'''
