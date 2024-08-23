from functools import reduce



def _avg(nums: list[int | float]) -> int | float:
    return sum(nums)/len(nums)


def _product(nums: list[int | float]) -> int | float:
    return reduce(lambda x, y: x * y, nums)

