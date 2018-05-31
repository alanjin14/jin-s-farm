first = input()
second = input()
third = input()
forth = input()
forthTele = first == '8' or first == '9'
lastTele = forth == '8' or forth == '9'
secondThirdTele = second == third
ifTele = forthTele and lastTele and secondThirdTele
if(ifTele):
    print('Ignore')
else:
    print('Answer')