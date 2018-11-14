"""Write a program that computes the net amount of a bank account based
a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""

netamount=0
while True:
    x=input()
    if not x:
        break
    d=x.split(' ')
    l=d[0]
    w=d[1]
    if(l=='D'):
        netamount+=int(w)
    elif(l=='W'):
        netamount-=int(w)
print(netamount)