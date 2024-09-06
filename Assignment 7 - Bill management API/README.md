# Bill Management - Django API

Bill Management API for you that helps you to maintain you bills when you are enjoying with others, so don't take burden to manage bills, use this API to make you life simple!

### Note: Postman export is provided thath have each API with its showcase and explanation!


##  **What it includes:**

<h3 id="split_evenly">Split Evenly</h3>
Divide total bill with no of people, simple and effective.

<h3 id="split_unevenly">Split Un-Evenly</h3>
Take each person contribution to bill and divide bill between all of them. 

- Positive value means that person needs to pay more.
- Negative value means that person should receive that amount.

<h3 id="tip_tax_with_even_split">Tip & Tax With Even Split</h3>
Add given tip and tax(as rate) in total bill, if 0 then total remain unchanged, and then split bill evenly.

<h3 id="discount_with_even_split">Discount With Even Split</h3>
Use Discount(as rate) to get new total bill and then split evenly.

<h3 id="shared_items_with_un_even_split">Shared Items With Un-Even Split</h3>
5. Shared items with uneven split: Split amount  of each shared item between sharing people. You can give item name to disgusting between items, then a total amount(number) and then peoples with their name and their contribution, you can give as many you want, just make sure to keep each shared-item in dict that in list of shared-items, each dict represent each item.

- In result, we get each shared-items with sharing people in which each person has it money, like _[Split Un-Evenly](#split_unevenly)_ where positive means to pay that amount and negative for receiving amount.


## Dependencies:
- Python 3.10+

> _Virtual Environment for dependencies is recommened!_

- **Django**: `pip install django`


## How to run this?

Open termianl/cmd in same folder of this program.
- `cd BillMage`: Change your directory to locate `manage.pg`
- `python manage.py runserver`: It will host a local server at `8000`, for custom port, provide that port at the end.

## Bill Opr

- Use `bill_opr/` param to access operations.
There are five operation that can perform by **POST** HTTP method.
1. `split-evenly/` : [Read Split Evenly](#split_evenly)
2. `split-unevenly/` : [Read Split Un-Evenly](#split_unevenly)
3. `split-including-tip-tax/` : [Read Tip & Tax With Even Split](#tip_tax_with_even_split)
4. `split-with-discount/` : [Read Discount With Even Split](#discount_with_even_split)
5. `uneven-split-with-shared-items/` : [Read Shared Items With Un-Even Split](#shared_items_with_un_even_split)


---
## [Saadullah Khan.](https://www.linkedin.com/in/Saadullahkhan3)