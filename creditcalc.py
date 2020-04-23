# write your code here
import math
def repay(principal, payment):
    months = round(principal / payment)
    if int(months) == 1:
        return f'It takes {months} month to repay the credit'
    else:
        return f'It takes {months} months to repay the credit'


def payment(principal, months):
    count = math.ceil(principal / months)
    if count * months != principal:
        last_payment = round(principal - (months - 1) * count)
        return f'Your monthly payment = {count} with last month payment = {last_payment}'
    else:
        return f'Your monthly payment = {count}'


print('Enter the credit principal:')
principal_credit = int(input())

print('What do you want to calculate?')
print('type "m" - for count of months,')
print('type "p" - for monthly payment: ')
calc = input()
if calc == 'm':
    print('Enter monthly payment: ')
    monthly_payment = int(input())
    print(repay(principal_credit, monthly_payment))
else:
    print('Enter count of months: ')
    count_months = float(input())
    print(payment(principal_credit, count_months))