for i in range(1, 11):
    print(i)
b=0
while b<=10 :
    b+=1
    print(b,"fff")


x=15
if x>10:
    print("big")
else:
    print("small")

nums=[3,7,10,15]
if len(nums)>=4:
    print(nums)

n=5
b=0
while b<11 :
    print(b*n)
    b+=1

n = 7
while n > 0:
    print(n)
    n -= 1


words = ["cat", "dogs", "mouse"]

for w in words:
    print(w + "!")


for l in range(2,100,2):
    print(l)
count=0
o=[1,2,3,4,5,6,7,8,9,7,7,7]
for v in o:
    if v==7:
        count+=1
        print("rr",count)
    else:
        print("dd")

for k in range(1,100):
    if k%2==0:
        print(k)