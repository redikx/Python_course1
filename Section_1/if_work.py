name = input("What is your name : ")
age = int(input("What is your age : "))

if name and age:
    if 18 <= age < 31:
        print("You are allowed to go for 18-30 holidays")
    else:
        print("Unfortunately you are not allowed to go for 18-30 holidays")
else:
    print("You haven't enetered all information")