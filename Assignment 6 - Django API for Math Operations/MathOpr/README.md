# Commands - Run Files


<details>
<summary style="list-style: none; color: #da7d27">

## **[ Initial Server Start Steps ]**
</summary>

Run below command to start server 
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

Make sure to also check the port_no in [`demo.py`](./demo.py)


</details>

---

<details>
<summary style="list-style: none; color: #da7d27">

## **[ Test Cases - Demo ]**
</summary>

After the Server start, you can run [`demo.py`](./demo.py) to run test cases for the **API**.
_Run in anther terminal/cmd window, **not  close the server terminal/cmd it will terminate our localhost!**_

```
python ./demo.py
```
</details>

---
## [Saadullah Khan.](https://www.linkedin.com/in/Saadullahkhan3)
