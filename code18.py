"""A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""

x=input()
l=x.split(',')
flag1=flag2=flag3=flag4=0
d=[]
for i in l:
    for j in i:
        if j.isalpha():
            flag1=1
        elif j.isdigit():
            flag2=1
        elif j=='#' or j=='$' or j=='@':
            flag3=1
        else:
            flag4=1
    if flag1==1 and flag2==1 and flag3==1 and flag4!=1 and len(i)>=6 and len(i)<=12:
        d.append(i)
print(','.join(d))