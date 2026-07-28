
"""INSTRUCTIONS"""

# Given a loan amount, annual interest rate percentage, and fixed monthly payment, return an array of remaining balances after each monthly payment until the loan is paid off.

#     Each month, interest is calculated on the remaining balance using the monthly interest rate: (annual rate / 100) / 12, then the monthly payment is subtracted.
#     Return each remaining balance rounded to the nearest dollar.
#     Include the loan amount in the returned array. The first element in the array will always be the loan amount, and the last element of the array will always be 0.

def get_loan_schedule(loan, annual_interest, monthly_payment):
    monthly_interest_rate = (annual_interest / 100) / 12
    current_loan = loan
    all_balances = [loan]

    while current_loan > 0:
        monthly_interest_payment = monthly_interest_rate * current_loan
        balance_owed = (current_loan + monthly_interest_payment) - monthly_payment
        if round(balance_owed) < 0:
            all_balances.append(0)
        else:
            all_balances.append(round(balance_owed))
        
        current_loan = balance_owed 

    print(all_balances)

get_loan_schedule(50000, 5.2, 1650)

# Tests:

#     Waiting: 1. get_loan_schedule(1000, 0, 200) should return [1000, 800, 600, 400, 200, 0].
#     Waiting: 2. get_loan_schedule(1000, 5, 200) should return [1000, 804, 608, 410, 212, 13, 0].
#     Waiting: 3. get_loan_schedule(10, 50, 1) should return [10, 9, 9, 8, 8, 7, 6, 5, 5, 4, 3, 2, 1, 0, 0].
#     Waiting: 4. get_loan_schedule(5500, 8, 400) should return [5500, 5137, 4771, 4403, 4032, 3659, 3283, 2905, 2525, 2141, 1756, 1367, 977, 583, 187, 0].
#     Waiting: 5. get_loan_schedule(50000, 5.2, 1650) should return [50000, 48567, 47127, 45681, 44229, 42771, 41306, 39835, 38358, 36874, 35384, 33887, 32384, 30874, 29358, 27835, 26306, 24770, 23227, 21678, 20122, 18559, 16990, 15413, 13830, 12240, 10643, 9039, 7428, 5810, 4186, 2554, 915, 0].