#create a list
numbers=[1,3,4,2,5]

#create a variable then initialize
total = 0

#create a loop to loop from 0 to length of the list
for i in range(0,len(numbers)):
    """
    condition of the loop
    the final total=the initial total + the number the index chooses
    after the first process, the initial total will be the result from the previous process
    """

    total=total+numbers[i]

#print the final result of the loop
print(total)
