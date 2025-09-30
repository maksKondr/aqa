a = 5
print(type(a))

q =3.14
print(type(q))

w="pauli galtieri"
e=True
print(type(w))
print(type(e))

lst = [1,2,3,4,5]
lst2 = ["my","name","Gabaguli"]
print(type(lst))
print(type(lst2))

tpl = (1,2,3)
print(type(tpl))

dct = {"name":"tiny","age" : 50}
print(type(dct))

set_ex = {1,2,3}
print(type(set_ex))


class Person:
    pass
o=Person()
print(type(o))


Lst =(1,2,3,4,5)
dOT = {"name":"tony","age":5}
res=dOT["age"] in Lst
print(res)

gang = "sopranos"
yyy= "pussy"
kils = 228
bandits = ("tony","pauli","silvio","junior")
leaders = {"papa":"tony","capo":"silvio","secondname":"sopranos"}
z= leaders["papa"] in bandits and kils==223 or leaders["capo"] in bandits and leaders["secondname"]==gang
print(z)