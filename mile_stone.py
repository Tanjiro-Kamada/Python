# Create a class called Payroll whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Create 5 different class methods which will calculate the payee, nhif_deductions, nhdf_deductions, nssf_deductions, gross_salary and net_salary. 
# NB: Use KRA, NpHIF and NSSF values provided in the links above.

class Payroll:
    def __init__(self, basic_salary, benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits

    def gross_salary(self):
        return self.basic_salary + self.benefits

    def payee(self):
        gross = self.gross_salary()
        if gross <= 24000:
            return gross * 0.1
        elif gross <= 32333:
            return (gross - 24000) * 0.25 + 2400
        else:
            return (gross - 32333) * 0.3 + 2400 + 2083.25

    def nhif_deductions(self):
        gross = self.gross_salary()
        if gross <= 5999:
            return 150
        elif gross <= 7999:
            return 300
        elif gross <= 11999:
            return 400
        elif gross <= 14999:
            return 500
        elif gross <= 19999:
            return 600
        elif gross <= 24999:
            return 750
        elif gross <= 29999:
            return 850
        elif gross <= 34999:
            return 900
        elif gross <= 39999:
            return 950
        elif gross <= 44999:
            return 1000
        elif gross <= 49999:
            return 1100
        elif gross <= 59999:
            return 1200
        elif gross <= 69999:
            return 1300
        elif gross <= 79999:
            return 1400
        elif gross <= 89999:
            return 1500
        elif gross <= 99999:
            return 1600
        else:
            return 1700

    def nssf_deductions(self):
        nssf_rate = min(self.gross_salary() * 0.06, 1080)
        return nssf_rate

    def net_salary(self):
        total_deductions = self.payee() + self.nhif_deductions() + self.nssf_deductions()
        net_salary = self.gross_salary() - total_deductions
        return net_salary

# Example usage:
basic_salary = 50000
benefits = 10000

payroll = Payroll(basic_salary, benefits)
print("Gross Salary: ", payroll.gross_salary())
print("Payee: ", payroll.payee())
print("NHIF Deductions :", payroll.nhif_deductions())
print("NSSF Deductions :", payroll.nssf_deductions())
print("Net Salary: ", payroll.net_salary())

