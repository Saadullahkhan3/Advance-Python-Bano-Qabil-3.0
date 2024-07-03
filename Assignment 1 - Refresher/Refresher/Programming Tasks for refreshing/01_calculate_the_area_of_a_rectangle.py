
def rectangle_area(length, width):
    return length * width


length = int(input("Enter the Length of the rectangle: "))
width = int(input("Enter the Width of the rectangle: "))

rec_area = rectangle_area(length=length, width=width)

print(f"The area of the rectangle is: {rec_area}")

# Output:
'''
Enter valid numbers only!
Enter the Length of the rectangle: 5
Enter the Width of the rectangle: 3
Area of the rectangle with 5 lenght and 3 Width is -> 15
'''
