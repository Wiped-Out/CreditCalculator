import argparse
import sys
from math import ceil, log


def diff_payment(principal, periods, interest):
    nominal_rate = interest / (12 * 100)
    overpayment = 0
    for payment_months in range(1, periods + 1):
        payment = ceil(
            (principal / periods) + nominal_rate * (principal - (principal * (payment_months - 1)) / periods))
        overpayment += payment
        print(f'Month {payment_months}: paid out {payment}')
    return f'Overpayment = {ceil(overpayment - principal)}'


def count_of_months(principal, monthly, interest):
    nominal_rate = interest / (12 * 100)
    period_count = ceil(log(monthly / (monthly - nominal_rate * principal), 1 + nominal_rate))
    if period_count < 12:
        print(f'You need {period_count} months to repay this credit!')
        return f'Overpayment = {ceil((monthly * period_count) - principal)}'
    elif period_count % 12 == 0:
        print(f'You need {period_count // 12} years to repay this credit!')
        return f'Overpayment = {ceil((monthly * period_count) - principal)}'
    else:
        print(f'You need {period_count // 12} years and {period_count % 12} months to repay this credit!')
        return f'Overpayment = {ceil((monthly * period_count) - principal)}'


def annuity_payment(principal, periods, interest):
    nominal_rate = interest / (12 * 100)
    payment = ceil(
        principal * (nominal_rate * pow((1 + nominal_rate), periods)) / (pow((1 + nominal_rate), periods) - 1))
    print(f'Your annuity payment = {payment}!')
    return f'Overpayment = {ceil((payment * periods) - principal)}'


def credit_principal(monthly, periods, interest_rate):
    nominal_rate = interest_rate / (12 * 100)
    cred_principal = monthly / (
                (nominal_rate * pow((1 + nominal_rate), periods)) / (pow((1 + nominal_rate), periods) - 1))
    print(f'Your credit principal = {round(cred_principal)}!')
    return f'Overpayment = {ceil((monthly * periods) - cred_principal)}'


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="Type of calculation to be made")
parser.add_argument("--principal", help="credit principal", type=int)
parser.add_argument("--periods", help="month periods", type=int)
parser.add_argument("--payment", help="month periods", type=int)
parser.add_argument("--interest", help="interest rate", type=float)
args = parser.parse_args()

values = [x for x in vars(args).values() if x is not None]
values = values[1:]
values = [x for x in values if x < 0]

if len(sys.argv) <= 4:
    print('Incorrect parameters.')

elif len(values) > 0:
    print('Incorrect parameters.')

elif args.type == 'diff':
    principal = args.principal
    periods = args.periods
    interest = args.interest
    print(diff_payment(principal, periods, interest))

elif args.type == 'annuity' and args.principal and args.periods is not None:
    principal = args.principal
    periods = args.periods
    interest = args.interest
    print(annuity_payment(principal, periods, interest))

elif args.principal and args.payment:
    cred_principal = args.principal
    monthly_payment = args.payment
    interest_rate = args.interest
    print(count_of_months(cred_principal, monthly_payment, interest_rate))

elif args.type == 'annuity' and args.payment:
    payment = args.payment
    periods = args.periods
    interest = args.interest
    print(credit_principal(payment, periods, interest))

elif args.type != 'diff' or 'annuity':
    print('Incorrect parameters')
