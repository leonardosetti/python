""""
Programa para cálculo de ajustes de salário conforme dissídio e adiantamentos realizados pela Wipro.

TODO:
Refatorar código conforme PEP8
Traduzir labels do display
verificar logica de implementação.

Esta é uma implementção n00b, com base em objetivo específico do programador
"""

current_salary = eval(input(f"Insira o valor do seu salário atual:\nR$ "))
december_discount = eval(input(f"Insira o valor do adiantamento em 12/2018:\nR$ "))

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
    inss = ("%.2f" % 642.34)

diff_less_inss = (float(total_diff) - float(inss))

if diff_less_inss <= float(1903.99):
    irrf = "ISENTO"
elif diff_less_inss <= float(2826.65):
    irrf = (diff_less_inss * 0.075 - 142.8)
elif diff_less_inss <= float(3751.05):
    irrf = (diff_less_inss * 0.15 - 354.8)
elif diff_less_inss <= float(4664.68):
    irrf = (diff_less_inss * 0.225 - 636.13)
else:
    irrf = (diff_less_inss * 0.227 - 869.36)

print(f"Salary fix 2018:\nR$ {float(salary_fix_1):.2f}\n")
print(f"Salary fix 2019: R$' + f'{float(salary_fix_2):.2f}\n")
print(f"The difference without taxes: R$' + f'{float(total_diff):.2f}\n")
print(f"INSS: R$' + f'{float(inss):.2f}\n")

if irrf == "ISENTO":
    taxes = (float(inss))
    print(f"IRRF: {irrf}\n")
else:
    taxes = (float(inss) + float(irrf))
    print(f"IRRF:\nR$ {float(irrf):.2f}\n")

expected_incoming = (float(total_diff) - float(taxes) - float(december_discount))

print(f"Total extra incoming expected:\nR$ {float(expected_incoming):.2f}\n")
