string = "hellow world!"

if "hellow" in string :
    print("hellow in string")
else:
    print("hellow not found")


a=10
b=20

if a >=10 and b==20 or a+b== 24 :
    print(a+b)
else:
    print("u mama syka")



test_list = ["tony","maks",1,2,3,4]

if 1 in test_list and "tony" in test_list :
    print(len(test_list))
elif "gnida"not in test_list :
    print(test_list)
else:
    print("idiot")




z=10
x=20
c="one"
v="RDR"
print(len(c),len(v),z+x )

if z+x==50 or len(c)==z :
    print("first")
elif len(c)==len(v):
    print("good")
else:
    print("false")






gang1={
    "name": "sopranos",
    "leader" : "tony",
    "count" : 22,
    "kilss" : 228,
    "italians" : True
}

gang2={
    "name":"ny",
    "leader" : "johny",
    "count" : 50,
    "kilss" : 500,
    "italians" : False
}

gang3={
    "name":"old gvardia",
    "leader" : "phil",
    "count" : 10,
    "kilss" : 25,
    "italians" : False
}

leaders_FBI_list = ["Jim","silvio","gay","junior","pauli","tony","johny","phil"]

if gang3["name"] and gang3["leader"] and gang3["italians"] is True:
    if gang3["leader"]  not in leaders_FBI_list:
        print(f"the winer isss {gang3['leader']}")
    elif gang3["kilss"]>=300 or gang3["count"]==88 :
        print(gang3["kilss"])
    else:
        print("Tony Blondeto son of the bitch")
elif gang3["kilss"] ==0 :
    print("U died")
elif not gang3["italians"] == True:
    print("are u gay&")
else:
    print("its not really")

