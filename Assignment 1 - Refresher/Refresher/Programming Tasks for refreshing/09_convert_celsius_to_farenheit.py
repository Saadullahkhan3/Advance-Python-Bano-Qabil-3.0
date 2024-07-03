
def celsius_to_farenheit(celsius):
    farenheit = (celsius*1.8) + 32  # Exact Formula -> (celsius * 9/5) + 32
    return f"{farenheit:.2f}"


celsius_input = int(input(f"Enter temperature in Celsius : "))

print(f"Temperature in Farenheit is : {celsius_to_farenheit(celsius_input)}")

# Output:
'''
Enter temperature in Celsius : 37
Temperature in Farenheit is : 98.60
'''
