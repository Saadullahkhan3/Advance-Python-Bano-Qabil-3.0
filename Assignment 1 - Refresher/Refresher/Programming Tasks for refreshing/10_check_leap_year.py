
def is_leap_year(year: int):
    if year % 4 == 0:
        return True
    
    return False


year_input = int(input(f"Enter a year : "))

leap_year_or_not = "a Leap year" if is_leap_year(year_input) else "not a Leap year"

print(f"{year_input} is {leap_year_or_not}")

# Output:
'''
Enter a year : 2020
2020 is a Leap year
'''
