'''
Question 2: Given a list of numbers [2, 4, 6, 8, 10], first use the map function and a lambda function to double each number. Then, use the reduce function to find the product of the doubled numbers.

- Input: [2, 4, 6, 8, 10]
- Expected Output: 46080 (Product of [4, 8, 12, 16, 20])

*Note: Expected Output is wrong, see below calculation:
2 x 4 x 6 x 8 x 10 = 3,840
4 x 8 x 12 x 16 x 20 = 122,880

'''

from functools import reduce    # reduce is found in functools built-in library.


nums: list[int] = [2, 4, 6, 8, 10]

doubled_nums: list[int] = list(map(lambda x: x*2, nums))

reduced_product: int = reduce(lambda x, y: x * y, doubled_nums)

print(f"Output: {reduced_product} (Product of {doubled_nums})")


# Output:
'''
Output: 122880 (Product of [4, 8, 12, 16, 20])
'''
