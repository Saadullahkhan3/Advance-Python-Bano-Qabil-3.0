
def fibonacci(number: int):
    if number == 0:
        return [0]
    
    if number == 1:
        return [0, 1]

    f0 = 0
    f1 = 1
    fn = int()
    fib = [0, 1]

    for i in range(2, number):
        fn = f0 + f1
        f0 = f1
        f1 = fn
        
        fib.append(fn)
    
    return fib


num_input = int(input("Enter the number of terms : "))

print(f"Fibonacci Series up to {num_input} terms : {fibonacci(num_input)}")

# Output:
'''
Enter the number of terms : 10
Fibonacci Series up to 10 terms : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''
