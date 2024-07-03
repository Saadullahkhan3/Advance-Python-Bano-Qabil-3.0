from datetime import datetime


def day_name_by_day_no(day_no: int) -> str:
    '''
    Take the number of day 1-7 and return the day name e.g 1 -> Mon

    Args:
        day_no: int -> Day number 1 to 7

    Returns:
        Day name of the given day number
    '''

    match day_no:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case _:
            return "Sunday"
        

def find_day_of_week(date_str: str) -> str:
    '''
    Note: If your month or date are single digit number so not inculde 0 at the beginning. e.g: 05 -> 5

    Take the date in 'YYYY-mm-dd' format and return the day name

    Args:
        date_str: str -> Should be in 'YYYY-mm-dd' format

    Returns:
        day_name: str -> Name of the day according to given date 
    '''
    
    return day_name_by_day_no(datetime.strptime(date_str, "%Y-%m-%d").weekday())



def main() -> None:
    print("\n >> Note: If your month or date are single digit number so not inculde 0 at the beginning. e.g: 05 -> 5 \n")

    date_input = input("Enter date in 'YYYY-MM-DD' format. \nEnter here : ")
    
    print(f"Day name of this date {date_input} is {find_day_of_week(date_input)} \n")


if __name__ == "__main__":
    main()
  

# Output:
'''

 >> Note: If your month or date are single digit number so not inculde 0 at the beginning. e.g: 05 -> 5

Enter date in 'YYYY-MM-DD' format.
Enter here : 2010-5-9
Day name of this date 2010-5-9 is Saturday 

'''
