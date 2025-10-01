test_list =[1,2,3,4,5,6]

for num in test_list:
    print(num**2 ,"----*")

a=0
while a<10:
    a+=1
    print(a)



test_list1=[1,2,3,4,5,6,7,8,9]
while len(test_list1)<12:
    test_list1.append(1)
    print(test_list1)


b=0
add_list= []

while len(add_list)<100:
    print(len(add_list))
    add_list.append(b)
    b+=1
    if len(add_list)==50:
        print("u are in midle")

