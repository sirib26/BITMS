'''def table():
    for i in range(1,11):
        print(i,"* 10 = ",i*10)
table()'''
'''def leap():
    year=int(input("enter the year:"))
    if(year%400==0 ):
        print("it is leap year")
    elif(year%100==0):
        print("it is not a leap year")
    elif(year%4==0):
        print("leap year")
    else:
        print("not a leap year")
leap()}'''
'''email=["siri","sanju","uzma"]
password=["1234"]
name="siri"
count1=name.count("i")
print(count1)
se=email.count("sirgi")
print(se)'''
'''class Mango:
    def __init__(self):
        print("this is what?")
    def balaji(self):
        print("this is without para")
    def siri(self,a,b):
        print(a+b,"this is with para")
man=Mango()
man.balaji()
man.siri(2,2.5)'''
n=int(input("enter a number"))
isprime=False
for i in range(2,n):
    if i%n==0:
        isprime=True
        break
if isprime:
    print(" not a prime number")
else:
    print("prime number")
    rev=1
    temp=n
    while n!=0:
        rem=n%10
        rev=(rev*10)+rem
        n//=10
        print(rev)
        if(temp==rev):
            print("magical prime")
        else:
            print("not a magical prime")
    
      