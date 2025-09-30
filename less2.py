name = "Tony"
user_email = "qweqw@eefe.effe"
Name = "gandon"
print(name,user_email,Name)


num_1 = 100
num_2 = 10
num_3 = num_1 + num_2
#додавання
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 - num_2
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 * num_2
#множення
print(num_3)

num_1 = 100
num_2 = 10
num_3 = num_1 / num_2
#ділення
print(num_3)

num_3 = 7
num_4 = 2
num_5 = num_3 / num_4  #звичайне ділення
num_6 = num_3 // num_4 #ділення без залишку
print(num_5,num_6 )

num_7 = 5
num_8 = 2
num_9 = num_7 ** num_8  #приподнести до степіння
num_10 = num_7 % num_8  #залишок із ділення тут 7 / 2 і залишок буде 1 бо 2+2+2 = 6 і іщє 1 є а якшо мми ділим 6 і 3 то результат буде 0 бо 3+3 6

print(num_9,num_10)


num_11 = 10
num_12 = 5
num_13 = num_11==num_12  # чі рівні ці значення
num_14 = num_11 != num_12  # чі НЕ рівні ці значення
num_15 = num_11 < num_12
num_16 = num_11 > num_12
print(num_13,num_14,num_15,num_16)



result = num_11>5 and name=="Tony"
result1= num_11>5 or name=="Toy"
print(result,result1)

massage = "Tony got some dirty money"
result2 = name in massage  # перевіряємо чі є змінна name в меседжі
result3 = name not in massage
print(result2,result3)



age = 50
wife = "carmella"
secondName = "soprano"
print(age==50 and "c" in wife and secondName != "blundetto")