mylist=[1,2,3,4,5,6,7,8,9]
f=["cat","dog","banana","monkey"]
print(mylist[0],mylist[1],mylist[-1])
print(f[1])
print(mylist[1:-1],mylist[::2])
print(f[0:3:2])
print(mylist[::-1]) #обернений список
mylist.append(10) #append додавання до списку
f.append("rat")
print(mylist,f)
mylist.insert(-1,77) #insert вставляє в список вказуєш індекс і обьєкт
f.insert(1,"bob")
print(mylist,f)

mylist.remove(77)
f.remove("bob") #видаляє
print(mylist,f)

lastelem1=mylist.pop(1) #видаляє та повертає елемент за індексом
lastelem2=f.pop(1)
print(lastelem1,lastelem2)

print(mylist.index(1),f.index("monkey"))
mylist.extend([666,777,1000,777,777])
f.extend(["ggg","ice","yes"])
print(mylist.count(777),f.count("ggg")) #рахує кількість елемента

print(mylist,f)
mylist.sort(reverse=True) #SORT СОРТУЄ від меншого а реверс тру це його обертає
f.sort()
print(mylist,f)
mylist.reverse()
print(mylist) #обертає







q=(1,2,3,4,5,6,7,8,8,8,8,8,9) #кортеж не зміний
print(q.index(4))
print(q.count(8))







testDict={"user":"Tom","age":18,"coutry":"poland"}
print(testDict["user"],testDict["age"],testDict.get("coutry"))
print(testDict.get("animal","key not found"))
testDict["age"]=30 #зміна значення в словнику через вказання ключа і нового значення
print(testDict)
testDict["animal"]="cat"
print(testDict)
testDict.pop("animal")
print(testDict)
copy_test=testDict.copy()
testDict.clear()
print(testDict)
print(copy_test)

for key , value in copy_test.items():
    print({key} , {value})

