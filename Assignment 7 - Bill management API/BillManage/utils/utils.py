

def even_split(total: int | float, 
               no_of_people: int) -> int | float:
    '''Use to split an amount equally between peoples by their quantity, then return it'''
    return total / no_of_people


def add_tax(amount: int | float, 
            tax_rate: int | float) -> int | float:
    '''Use to add tax by its rate to amount, then return it'''
    return amount + (amount * tax_rate / 100)


def add_discount(amount: int | float, 
                 discount_rate: int | float):
    '''Use to add discount by its rate to amount, then return it'''
    return amount - (amount * discount_rate / 100)

