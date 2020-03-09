#checks username is new or not
#checks whether password satisfies all requirements

old=['abc123','cdnj12#','dkcmk@','jndjvn%','ddndnioe3'] #List of previous usernames
user=input('Enter username') 
password=input('Enter password')
for each in old:                                       #checks whether username matches with old usernames
    if user==each:
        print('Enter a new username')
    break
l=len(password)
lnew=0
for each in password:
    if each.isalnum():
        lnew=lnew+1
if l<20 and l>4:
    n=0
    for each in password:
        if each.isdigit():
            n=n+1
    if n:
        if l==lnew:
            print('password does not contain special character')
        else:
            print('password accepted')
    else:
        print('Atleast one digit is required in passsword')
else:
    print('create a password with range of 5 to 19 characters')