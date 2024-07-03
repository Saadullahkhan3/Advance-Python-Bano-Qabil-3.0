# Note: ChatGPT ONLY helps in formula. Code/Program is Original

def calc_profit(amount: float|int, rate: float|int, year: float|int) -> float:
    r = rate/100
    profit = amount * r * year 
    return profit
 

def main():
    try:
        amount_input = float(input("Enter the principal amount : "))
        rate_input = float(input("Enter the rate of interest : "))
        year_input = float(input("Enter the time period in years : "))

        print(f"Simple Profit : {calc_profit(amount_input, rate_input, year_input)}")
    except:
        print("~~~{ Opps! : Input Error, but you can enter values again :) }~~~" + "\n" + "Enter Again!")
        main()


if __name__ == "__main__":
    main()

# Output:
'''
Enter the principal amount : 1000
Enter the rate of interest : 5
Enter the time period in years : 2
Simple Profit : 100.0
'''
