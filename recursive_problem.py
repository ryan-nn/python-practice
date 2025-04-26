
#create a function with an if statement
def factorial(n):
    """
    if n==o or n==1 the result should be 1
    since factorial of o and factorial of 1 is 1
    we cant use and because a number in this case n cannot be 0 and 1
    """
    if n==0 or n==1:
        return 1 #factorial of 0 or 1 is 1
    else:
        """
        n * factorial(n-1) that is n is multiplied by factorial n-1
        if n was 4
        4 * 3! which is 4 x 3 x 2 x 1 
        """
        return n* factorial(n-1) #process to calculate the factorial and return the result

#prompt the user to enter a number
number=int(input("Enter number: "))

"""
print the result
number becomes n when you call the function while passing number as your parameter
"""
print(f"Factorial of {number} is", factorial(number))
