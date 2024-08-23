# Assignment 6
## **API for Math operations - Django API**

I am so happy that I finally stepped in API creation!

> Use [`demo.py`](./demo.py) for the example usage, make sure to check the `url` and `payload` according to you.

### **What it does?**
We can able to do some below listed math based tasks through our **[ GET | POST ]** **API** created in `django` framework:
- `total` -> Total of the given numbers list.
- `avg` -> Avg of the given numbers  list.
- `product` -> Product of the given numbers  list.

<details>
<summary style="list-style: none; color: #da7d27">

## **[ API Endpoints: ]**
</summary>

### **Base Part**
For the main base part for the url we can run our server at `localhost`
```
python ./manage.py runserver
```
It will spin server at `8000` port, if you want to use another port pass next to the `runserver` command
```
python ./manage.py runserver <port-no>
```

Now, we get our base part that will be in below format:
```
http://127.0.0.1:<port-no>
```
_Default_
```
http://127.0.0.1:8000
```

Make sure to also check the port_no in [`demo.py`](./demo.py)

### **Math Opr**
For using math operations we need to use `math_opr` as param to access required endpoints
```
http://127.0.0.1:<port-no>/math-opr/
```

### **Methods**
Now, we have three options:
1. `total/` -> Return total/sum of the given numbers(iterables)
2. `avg/` -> Return avg of the given numbers(iterables)
3. `product/` -> Return product of the given numbers(iterables)

**Payload data schema**
> *nums can contain any numbers in iterable data set.
```json
{"nums": [1, 2, 3, 4, 5]}
```
</details>



<details>
<summary style="list-style: none; color: #da7d27">

## **[ Files Structure: ]**
</summary>

- `Djagno` required files.
- `math_opr` *django app* for the math operations.
- `utils` Custome Python package for the project, includes:
    - `utils.py` for general use. 
    - `math_opr` include functions for the `math_opr` app.


</details>


---
## [Saadullah Khan.](https://www.linkedin.com/in/Saadullahkhan3)
