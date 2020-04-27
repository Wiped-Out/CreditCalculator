#!/usr/bin/env python

from math import log, ceil


def count_of_months():
    try:
        credit_principal = int(input('Enter credit principal: '))
        monthly_payment = int(input('Enter monthly payment: '))
        credit_interest = float(input('Enter credit interest: '))
        nominal_rate = credit_interest / (12 * 100)
        period_count = ceil(
            log(monthly_payment / (monthly_payment - nominal_rate * credit_principal), 1 + nominal_rate))
        if period_count < 12:
            return f'You need {period_count} months to repay this credit!\n'
        else:
            return f'You need {period_count // 12} years and {period_count % 12} months to repay this credit!\n'
    except ValueError:
        return "Cannot calculate negative values.\n"


def annuity_payment():
    credit_principal = int(input('Enter credit principal: '))
    periods = int(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    nominal_rate = credit_interest / (12 * 100)
    payment = credit_principal * (nominal_rate * pow((1 + nominal_rate), periods)) / (
                pow((1 + nominal_rate), periods) - 1)
    return f'Your annuity payment = {ceil(payment)}!\n'


def credit_principal():
    monthly_payment = float(input('Enter monthly payment: '))
    periods = int(input('Enter count of periods: '))
    credit_interest = float(input('Enter credit interest: '))
    nominal_rate = credit_interest / (12 * 100)
    principal = monthly_payment / (
                (nominal_rate * pow((1 + nominal_rate), periods)) / (pow((1 + nominal_rate), periods) - 1))
    return f'Your credit principal = {round(principal)}!'


choices = {'n': count_of_months, 'a': annuity_payment, 'p': credit_principal}
while True:
    print('''What do you want to calculate?
    type "n" - for count of months,
    type "a" - for annuity monthly payment,
    type "p" - for credit principal,
    type "exit" - to exit the program:''')
    usr_input = input('> ').lower()
    if usr_input == 'exit':
        break
    else:
        print(choices[usr_input]())
