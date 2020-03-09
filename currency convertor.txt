#currency conversion 

choicei=input('Enter 1 for to convert to rupee,2 to convert from rupee') #input from user to convert from rupee or to convert to rupee
a=[71.64,51.28,0.65,78.14] # values of different currencies to INR
if choicei=='1': 
    choice=input('select 1 for USD to INR\n 2 for SGD to INR\n 3 for YEN to INR\n 4 for EUR to INR')
    den=int(input('Enter your denomination ')) #getting denomination
    if choice =='1' or '2' or '3' or'4':
        print('you have {} rupees'.format(den*a[int(choice)-1])) #getting value by indexing
    else:
        print('invalid input')
elif choicei=='2':
    choice=input('select 1 for INR to USD\n 2 for INR to SGD\n 3 for INR to YEN\n 4 for INR to EUR')
    den=float(input('Enter your denomination ')) #getting denomination
    b=['USD','SGD','YEN','EUR'] #List of strings
    if choice =='1' or '2' or '3' or'4':
        print('you have {0} {1} '.format((den/a[int(choice)-1]),b[int(choice)-1])) #getting value by indexing
    else:
        print('invalid input')