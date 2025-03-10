height=int(input("enter a height"))
if height > 120:
    print("your eligible")
    age=int(input("enter your age: "))
    if age <= 12:
        bill=100
        print("you pay 100")
    elif age <= 18:
        bill = 200
        print("you pay 200")
    elif 55<=age and 65>=age:
        bill =0
    else:
        bill =500
        print('you pay 500')
    photo=input("you will take the photo yes y no n: ")
    if photo == "y":
        bill =bill+50
    print(f"your bill is {bill}")