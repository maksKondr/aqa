user_1= {
    "user_name" : "Tester",
    "role" : "admin",
    "conection" : True
}
user_2= {
    "user_name" : " Tom",
    "role" : "user",
    "conection" : True
}
user_3= {
    "user_name" : "dev",
    "role" : "pro_user",
    "conection" : False
}
list_of_users = [user_1,user_2,user_3]

for user in list_of_users:
    print(f"work with{user['user_name']}")
    if not user["conection"]:
        count_of_tries = 10
        while count_of_tries !=0:
            print("try conect")
            count_of_tries-=1
            print("u try",count_of_tries)
    if user["role"]=="admin":
        print(f"heloow {user['user_name']}")
    else:
        print("what&")
print("end")