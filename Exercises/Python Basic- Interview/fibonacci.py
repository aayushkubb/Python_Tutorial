n = input("Enter n value: ") 
n = int(n)
if(int(n)<3):
    while(n):
        print(1)
        n -= 1
else:
    a,b = 1,1
    print(a)
    for i in range(int(n)-1):
        print (b)
        a,b=b,a+b        
    