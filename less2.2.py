num_1 = "1"

print(type(num_1))

num_1=int(num_1)
print(num_1)
print(type(num_1))

num_1=float(num_1)
print(num_1)
print(type(num_1))

word="hellow world my boy"
print(len(word)) #len кількість символів
print(word.upper()) #.upper все з великої букви
word=word.capitalize()
print(word)
word=word.replace("my","that") #replace заміняє май на зет
print(word)
word=word.count("w")
print(word)
strinh=1
strinh=str(strinh)
print(type(strinh))




base_list = [1,2,3]
print(len(base_list))  #len скіки значень у списку
base_list.append(22)
print(base_list)

base_list.extend([4,5,6])
print(base_list)


base_dict = {"name":"tony" , "age":66 , "high": 180}
print(base_dict.keys())
print(base_dict.values())
print(base_dict.items())
print(base_dict.get("name"))
