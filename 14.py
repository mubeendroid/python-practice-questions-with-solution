"""Write a program that accepts a sentence and calculate the number of upper case
letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""

x=input()
counter1=0
counter2=0
for i in x:
    if(str(i).isupper()):
        counter1+=1
    elif(str(i).islower()):
        counter2+=1
print("UPPER CASE "+str(counter1))
print("LOWER CASE "+str(counter2))