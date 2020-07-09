#!/usr/bin/env python3

current_salary = eval(input('Type your current salary here: R$'))
print('')
december_discount = eval(input('Type 12/2018 advanced payment here: R$'))
print('')

adjustment_1 = 1.69
adjustment_2 = 5.07
inss = 0
irrf = 0
taxes = 0

part_diff_1 = ("%.2f" % (current_salary * (adjustment_1 / 100)))
part_diff_2 = ("%.2f" % (current_salary * (adjustment_2 / 100)))
salary_fix_1 = ("%.2f" % (current_salary + (current_salary * (adjustment_1 / 100))))
salary_fix_2 = ("%.2f" % (float(salary_fix_1) + float(salary_fix_1) * (adjustment_2 / 100)))
total_diff = ((float(part_diff_1) * 14) + (float(part_diff_2) * 7))

if total_diff <= float(1751.81):
    inss = ("%.2f" % (total_diff * 0.08))
elif total_diff <= float(2919.72):
    inss = ("%.2f" % (total_diff * 0.09))
elif total_diff <= float(5839.45):
    inss = ("%.2f" % (total_diff * 0.11))
else:
    inss = ("%.2f" % (642.34))

diff_less_inss = (float(total_diff) - float(inss))

if diff_less_inss <= float(1903.99):
    irrf = 'ISENTO'
elif diff_less_inss <= float(2826.65):
    irrf = (diff_less_inss * 0.075 - (142.8))
elif diff_less_inss <= float(3751.05):
    irrf = (diff_less_inss * 0.15 - (354.8))
elif diff_less_inss <= float(4664.68):
    irrf = (diff_less_inss * 0.225 - (636.13))
else:
    irrf = (diff_less_inss * 0.227 - (869.36))

print('Salary fix 2018: R$' + f'{float(salary_fix_1):.2f}')
print('Salary fix 2019: R$' + f'{float(salary_fix_2):.2f}')
print('The difference without taxes: R$' + f'{float(total_diff):.2f}')
print('INSS: R$' + f'{float(inss):.2f}')

if irrf == 'ISENTO':
    taxes = (float(inss))
    print(f'IRRF: {irrf}')
else:
    taxes = (float(inss) + float(irrf))
    print('IRRF: R$' + f'{float(irrf):.2f}')
print('')

expected_incoming = (float(total_diff) - float(taxes) - float(december_discount))

print('Total extra incoming expected: R$' + f'{float(expected_incoming):.2f}')
print('')
