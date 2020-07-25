s='Hello 456 rao 912 ramesh 1234xyz56789 hai 12'
i=0
while i<len(s):
    c=[]
    if s[i].isdigit():
        c.append(s[i])
        z=0
        each=i+1
        while z==0 and each<len(s):
            if s[each].isdigit():
                if int(s[each])==int(s[i])+1:
                    c.append(s[each])
                    each+=1
                    i+=1
                else:
                    break
            else:
                z=1
                break
    if len(c)>1:
        print(c)
    i+=1