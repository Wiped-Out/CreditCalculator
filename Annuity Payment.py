from math import log, ceil


def count_of_months(principal, monthly, interest):
    try:
        nominal_rate = interest / (12 * 100)
        period_count = ceil(log(monthly / (monthly - nominal_rate * principal), 1 + nominal_rate))
        if period_count < 12:
            return f'You need {period_count} months to repay this credit!'
        else:
            return f'You need {period_count // 12} years and {period_count % 12} months to repay this credit!'
    except ValueError:
        return "It's impossible to pay in a lifetime!"


def annuity_payment(principal, periods, interest):
    nominal_rate = interest / (12 * 100)
    payment = principal * (nominal_rate * pow((1 + nominal_rate), periods)) / (pow((1 + nominal_rate), periods) - 1)
    return f'Your annuity payment = {ceil(payment)}!'


def credit_principal(monthly, periods, interest):
    nominal_rate = interest / (12 * 100)
    principal = monthly / ((nominal_rate * pow((1 + nominal_rate), periods)) / (pow((1 + nominal_rate), periods) - 1))
    return f'Your credit principal = {round(principal)}!'


print('What do you want to calculate?')
print('''type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal:''')

usr_input = input()

if usr_input == "n":
    print('Enter credit principal: ')
    credit_principal = int(input())
    print('Enter monthly payment: ')
    monthly_payment = int(input())
    credit_interest = float(input('Enter credit interest: '))
    print(count_of_months(credit_principal, monthly_payment, credit_interest))

elif usr_input == "a":
    credit_principal = int(input('Enter credit principal: '))
    count_periods = int(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    print(annuity_payment(credit_principal, count_periods, credit_interest))

elif usr_input == "p":
    monthly_payment = float(input('Enter monthly payment: '))
    count_periods = int(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    print(credit_principal(monthly_payment, count_periods, credit_interest))
