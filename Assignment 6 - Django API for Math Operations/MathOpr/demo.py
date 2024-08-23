import requests as rq

# Change payload according to you
payload = {"nums": list(range(1, 11))}

# Make sure to check the port no, 8000 is default
port_no = "8000"
url = fr"http://127.0.0.1:{port_no}/math_opr/"


def formatted_title(str):
    return "\n" + "~"*20 + f" <{str}> " + "~"*20


total = rq.post(f"{url}total/", json=payload)
print(f"{formatted_title("TOTAL")} \n-> Total of '{payload['nums']}' is : {total.json()}")


avg = rq.post(f"{url}avg/", json=payload)
print(f"{formatted_title("AVG")} \n-> Avg of '{payload['nums']}' is : {avg.json()}")


product = rq.post(f"{url}product/", json=payload)
print(f"{formatted_title("PRODUCT")} \n-> Product of '{payload['nums']}' is : {product.json()}")


