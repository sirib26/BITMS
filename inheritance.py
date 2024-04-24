'''class a:
    def magical_prime(self, n):
        self.n = n
        isprime = False

        if n == 1:
            print(n, "is not a prime number")
        elif n > 1:
            for i in range(2, n):
                if n % i == 0:
                    isprime = True
                    break

        if isprime:
            print("not a prime number")
        else:
            print("prime number")
            temp = n
            rev = 0
            while n != 0:
                rem = n % 10
                rev = (rev * 10) + rem
                n //= 10
        isprime = False

        if rev == 1:
            print(rev, "is not a prime number")
        elif rev > 1:
            for i in range(2, rev):
                if rev % i == 0:
                    isprime = True
                    break
        if isprime:
            print("not a magical prime")
        else:
            print("magical prime")
            
obj = a()
n=int(input("enter a number"))
obj.magical_prime(n)'''
n = int(input("enter the number"))
if n<0:
    print("Wierd")
elif n>0:
    if n>1 and n<6:
        print("Not Weird")
    elif n>5 and n<21:
        print("Weird")
    elif n>20:
        print("Not Weird")


