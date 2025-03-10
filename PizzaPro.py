print(("Welcome to friends pizza shop"))

# Pizza size:
def size():
    size=input("What size pizza you wantt? S , M , or L: ")
    if size == "S":
        price = 100
    elif size == "M":
        price = 120
    elif size == "L":
        price=150
    return price

# Add peperoni :
def pepperoni(price):
    pepperoni = input("Do you want pepperoni on your pizza yes Y no N: ") 
    if pepperoni == "Y":
       price = price + 50
       return price

# Add extra cheese:      
def extra_cheese(price):
    extra_cheese = input("do you want extra cheese Y or N: ")
    if extra_cheese == "Y":
        price = price + 50
    print(f"your bill $ {price}")
# call the functions:        
price = size()
pepperoni(price)
extra_cheese(price)