num= int(input("Enter a number: "))

def cal_factorial (num):
    """
    this is the starting storage,
    it holds the running multiplication as you move through each number
    """
    factorial = 1

    """
    if the number is equal to 0 or equal to 1 return 1 
    """
    if num==0 or num==1:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial

print(f"Factorial of {num} is", cal_factorial(num))