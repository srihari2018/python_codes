def encrypt(s,n):
    a=''
    k=0
    for each in s:
        if ord(each)>96 and ord(each)<123:
            k=ord(each)+n
            if k>122:
                k=k-26
                a=a+chr(k)
            else:
                a=a+chr(k)
        else:
            a=a+each
    print(a)
def decrypt(s,n):
    a=''
    k=0
    for each in s:
        if ord(each)>96 and ord(each)<123:
            k=ord(each)-n
            if k<97:
                k=k+26
                a=a+chr(k)
            else:
                a=a+chr(k)
        else:
            a=a+each
    print(a)