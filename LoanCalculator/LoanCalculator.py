money_owed = float(input("The loan ammount ? "))
apr = float(input("What's the APR% ? "))
payment = float(input("How much you're monthly pay will be ? "))
months = int(input("How many months do you want to see the results for ? "))

monthly_interest_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_interest_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is:", money_owed)
        print('You paid off the loan in', i+1, 'months')
        break

    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest')
    print('Now I owe $', money_owed)