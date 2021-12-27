import datetime
import calendar


balance = 0
interest_rate = 0 
monthly_payment = 0
balance = int(input("Please enter your balance: "))
interest = int(input("Please enter interest rate: "))
monthly_payment = int(input("Please enter monthly payment: "))


today = datetime.date.today()

#added index is to get the total days of the month and otherwise (0, 31) would be outcome   
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
print(days_in_current_month)

# If we want to have first of next month
days_till_end_month = days_in_current_month - today.day
print(days_till_end_month)

# making a new variable
start_date = today + datetime.timedelta(days = days_till_end_month + 1)
print(start_date)

# end date variable (to pay off our balance e.g)
end_date = start_date
#creating a while loop to see how long would it take to pay off the balance.
while balance > 0:   #each time the beginning of new month will be stimulated
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment
#limiting our balance to 2 decimal 
    balance = round(balance, 2)
    if balance < 0:
        balance = 0
        
#The other way of writing: balance = 0 if balance < 0 else round(balance, 2)    
    print(end_date, balance)
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]  
    start_date = today + datetime.timedelta(days = days_till_end_month + 1)
    
    

