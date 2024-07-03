# Assignment 2
## Find the day name of the given date


> This Python program is capable to find the day name of the given date in `YYYY-MM-DD` format.

### Dependencies
- `Python 3 or newer` -> Python Programming Language, version 3 or newer
- `datetime` -> It is build-in module of Python

### Program Structure

<details>
<summary>

 ```python
main() -> None
```

</summary>
 This function is like control centre where we manage the input and invoke the functions.
</details>

---

<details>
<summary>

```python
find_day_of_week(date_str: str) -> str
```
</summary>

This function take the date and convert into *date object* and extract the weekday by `weekday()` function of *date object* and then **invoke** `day_name_by_day_no(day_no: int) -> str` that returns the day name.
</details>

---
<details>
<summary>

```python
day_name_by_day_no(day_no: int) -> str
```
</summary>

This function take the weekday and returns the day name. *Also this function use `match case statemensts` of Python that included in Python __3.10__*
</details>

---
## [Saadullah Khan.](https://www.linkedin.com/in/Saadullahkhan3)