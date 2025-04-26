#promt the user to enter their name which will be the string
string = input("Enter your name: ")

#create a string called reversed_string which is empty
reversed_string = ""

"""
this loop instructs the index to start picking characters from the last index iterating to the first index 
for example if the string inputed was JOHN we use the range(start, stop, step) whereby in this case 
start=len(string)-1 (start at the last index="N")
stop=-1   (stop just before index -1 that is index 0="J" ) 
step=-1   (move one step backwards each time)
so the loop will start by picking the letter "N" then "H" stoping at index 0 which is letter "J"
"""
for i in range(len(string)-1,-1,-1):

    """
    reverse_string= reversed_string + string[i] (since the string is empty it will be like,
    0 + string[i] which is indexing from the last index therefore, 
    0 + N
    N + H
    NH + O
    NHO + J
    storing the final result in reversed_string
    """
    reversed_string= reversed_string + string[i]

#print output
print(reversed_string)