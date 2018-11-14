"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""

x=input()
counter1=0
counter2=0
for i in x:
    if(str(i).isalpha()):
        counter1+=1
    elif(str(i).isdigit()):
        counter2+=1
print("LETTERS "+str(counter1))
print("DIGITS "+str(counter2))