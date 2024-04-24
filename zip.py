# python program to map two lists into a dictionary
# python program to check if a key exists in a dictionary or not
# print first letter of key basis using dictionary
# python program to count the Frequency of each word in a string using dictionary
'''list1=["siri","santosh"]
list2=["sanjana","uzma"]
res={key: value for key,value in zip(list1,list2)}
print(res)
test_string=input("enter a string:")
l=[]
l=test_string.split()
wordfeq=[l.count(p) for p in l]
print(dict(zip(l,wordfeq)))'''
'''list1 = ["sample_key", "test_key", "another_key"]
list2 = [1, 2, 3]

res = dict(zip(list1, list2))
print(res)

for i in res:
    if i.startswith('s'):
        print(i, end=' ')
    if i.endswith('i'):
        print(i)'''



'''my_dict={'apple' : 10, 'banana' : 20,'angel' : 30,'chennai':100,'balaji' : 100}

for key,value in my_dict.items():
    if key[2].lower() == 'l':
        print(f"the value of '{key}' is {value}")
        
        
d={'A' : 1,'B' : 2,'C' : 3}
key=input("enter key to check:")
if key in d.keys():
    print("key is present and value of the key is:")
    print(d[key])
else:
    print("key isn't present!")'''
# 1 python program to print sum of negative numbers, positive even numbers and positive odd numbers in a list
# 2 python program to print largest even and largest odd number in a list
'''input_string = input("Enter elements of the list separated by spaces: ")
original_list = [int(element) for element in input_string.split()]
print("List entered by the user:", original_list)

output_list = []
even_sum=0
neg_sum=0
odd_sum=0

for num in original_list:
    if num < 0:
        neg_sum += num
    elif num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

output_list.extend([neg_sum, even_sum, odd_sum])
print(output_list)'''
original_list = [int(element) for element in input("Enter elements of the list separated by spaces: ").split()]
print("List entered by the user:", original_list)

neg_sum, even_sum, odd_sum = sum(num for num in original_list if num < 0), sum(num for num in original_list if num % 2 == 0), sum(num for num in original_list if num % 2 != 0)

output_list = [neg_sum, even_sum, odd_sum]
print(output_list)

values=[2,4,1,-3,-5,7]
neg_values=max(i for i in values if i<0)
pos_values=max(i for i in values if i%2==0)
odd_values=max(i for i in values if i%2!=0)
print(neg_values,pos_values,odd_values)




IP: bitm college's located in ballari? Is't right!!!
OP: thgi rtsIira'l labnide ta colsege? ll'o cmtib!!!