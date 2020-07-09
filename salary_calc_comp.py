#!/usr/bin/env python3


class WageInc:

    gross_amount = None

    def __init__(self):
        self.gross_amount

    def wage_in(self):
        self.gross_amount = eval(input('Type your current salary here: R$'))


class CalcInss():
    inss = 0.0

    def inss_quota(self):
        if WageInc.gross_amount <= float(1751.81):
            self.inss = ("%.2f" % (WageInc.gross_amount * 0.08))
        elif WageInc.gross_amount <= float(2919.72):
            self.inss = ("%.2f" % (WageInc.gross_amount * 0.09))
        elif WageInc.gross_amount <= float(5839.45):
            self.inss = ("%.2f" % (WageInc.gross_amount * 0.11))
        else:
            self.inss = ("%.2f" % 642.34)


class FinSalary():
    wallet = None

    def __init__(self):
        self.wallet = ("%.2f" % (WageInc.gross_amount - CalcInss.inss))
        print(self.wallet)
