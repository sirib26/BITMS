'''siri=[]
n=int(input("enter the list size"))
for i in range(0,n):	#n means n-1 concept
    element=int(input("enter the elements"))
    siri.append(element)
print(siri)'''
'''default it will store as string with double quotes and list'''
'''siri=[1,2,10,4]
santosh=[5,6,7,8]
ss=siri+santosh
print(ss)
print(type(ss))
print(type(siri))
print(ss*2)
print(len(ss))
print(min(ss))
print(max(ss))'''
'''siri=[10,20,40]
sum=0
for i in siri:
    sum+=i
print(sum)'''
'''siri=[37,57,35,65]
sum=0
for i in siri:
    if i%10==7:
        print(i)'''
'''siri=[10,20,30,40]
santosh=[]
for i in siri:
    #if i not in santosh:
    santosh.append(i)	 #adding the elements at the end of the list
print(santosh)'''
'''two list 10 to 50 and 60 to 100 and 20'''
siri=[10,20,30,40,50]
santosh=[60,70,80,90,100,20]
siri=[]
n=int(input("enter the size"))
for i in range(0,n):
    ele=int(input("enter the elements"))
    siri.append(ele)
for i in siri:
    for j in santosh:
        if i==j:
            print(i)


