import random
letters = ["q","w","e","r","t","y","u","i","o","o","u","i","o","i","u","j","k","n","b","g","k","k","h","n","j","j","j"]
numbers = ["4","5","55","65","97","5","1","5","33","5","3","5","2","8","2","5","5","5","5","7","58","1","3","2","5"]
symbulse = ["!","@","#","^","&","*","()","-","_","+","=","/"]

How_many_letters = int(input("Hoe many letters?: \n"))
How_many_numbers = int(input("How_many_numbers?: \n"))
how_many_symbols = int(input("how_many_symbols: \n"))

# password = " "
# for i in range(0,How_many_letters+1):
#    password=password+random.choice(letters)
    
#for i in range(0,How_many_numbers):
 #   password=password+random.choice(numbers)
    
#for i in range(0,how_many_symbols):
#    password=password+random.choice(symbulse)
    
#print(password)

password_list = [ ]
for i in range(0,How_many_letters):
     password_list.append(random.choice(letters))
    
for i in range(0,How_many_numbers+1):
     password_list.append(random.choice(numbers))
    
for i in range(0,how_many_symbols+1):
     password_list.append(random.choice(symbulse))
    
print(password_list)
random.shuffle(password_list)
print(password_list)    
password = " "
for i in password_list:
    password=i+password
    
print(password)    

