"""Write a program which accepts a sequence of comma separated 4 digit binary numbers
as its input and then check whether they are divisible by 5 or not. The numbers that
are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010"""

x=input()
numbers=x.split(',')
values=[]
for p in numbers:
    intp=int(p,2)
    if(intp%5==0):
        values.append(p)
print(",".join(values))