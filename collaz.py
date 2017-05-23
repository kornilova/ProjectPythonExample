def collatz(number):
    if(number%2==0):
        return number//2
    else:
        return 3*number+1

print('Enter number:')
i=int(input())
while(i!=1):
    i=collatz(i)
    print(str(i))

