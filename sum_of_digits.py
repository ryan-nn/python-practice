def sum_of_digits_(number):
    """
    this checks if the number inputed by the user is 0
    it is also the base case when the recursion stops
    """
    if number == 0:
        return 0
    else:
        """
        if the number inputed by the user is 145 then
        number % 10=5 (it picks the last digit because " % " gives you the reminder
        when divided by 10 in this case its 5
        number//10 is integer division meaning no decimals just whole numbers
        sum_of_digits_(number//10) is the recursive case
        the first call:sum_of_digits_(145) in this case number=145
        145%10 = 5
        145//10 =14 (it would be 145/10 =14.5 but in this case no decimal
                     which from here we call the function again)
        the second call:sum_of_digits_(14) 
        14%10= 4
        14//10= 1
        the third call:sum_of_digits_(1) 
        14%10= 1
        14//10= 0
        the fourth case:sum_of_digits_(0) 
        base case reached 
        returns 0
        sum_of_digits_(0)=0
        sum_of_digits_(1)1+0=1
        sum_of_digits_(14)1+4=5
        sum_of_digits_(145)5+5=10
        10 which is the answer 
        """
        return (number % 10) + sum_of_digits_(number//10)

#prompt the user to enter a number
number= int(input("Enter number: "))

#abs(number)makes sure the number is positive even if the user enters a negative number
result= sum_of_digits_(abs(number))


print(f"The sum of the digits of {number} is ",result)
