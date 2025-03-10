def get_input():
    while True:
        try:
            initial_investment=int(input("Enter a initial inverstment:"))
            monthly_contribution=int(input("Enter a monthly contrybution:"))
            length_of_the_year=int(input("Enter a length of the year:"))
            interest_rate=int(input("Eenter a interest rate:"))
            return initial_investment,monthly_contribution,length_of_the_year,interest_rate
        except ValueError:
            print("Enter a valid input")
        
 
 #calculate compounding interest:       
def calculation(initial_investment,monthly_contribution,length_of_the_year,interest_rate):
        year_zero=0
        currency_symbol='$'
        year_contribution=monthly_contribution*12
        total_contribution=initial_investment
        future_value=initial_investment
        for i in range(1,length_of_the_year+1):
            total_contribution=total_contribution+year_contribution
            interest=future_value*interest_rate/100
            future_value=interest+year_contribution+future_value
            printing(year_zero,currency_symbol,interest_rate,initial_investment,i,total_contribution,future_value)
            
# print future values 
def printing(year_zero,currency_symbol,interest_rate,initial_investment,i,total_contribution,future_value):
        if i==1:
            print("Year\tTotal contribution\tFuture value","(",interest_rate,"% )")
            print(f"{year_zero}\t{currency_symbol}{initial_investment:,.2f}\t\t{currency_symbol}{initial_investment:,.2f}")
        print(f"{i}\t{currency_symbol}{total_contribution:,.2f}\t\t{currency_symbol}{future_value:,.2f}")
        
#Function called:
initial_investment,monthly_contribution,length_of_the_year,interest_rate=get_input()
calculation(initial_investment,monthly_contribution,length_of_the_year,interest_rate)
initial_investment,monthly_contribution,length_of_the_year,interest_rate=get_input()
calculation(initial_investment,monthly_contribution,length_of_the_year,interest_rate) 
   







