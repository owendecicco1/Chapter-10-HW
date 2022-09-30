import EmployeeClass as ec
import PayrollDeductionClass as pdc

employee = ec.Employee("Jimmy Smith", 58475, "Information Systems", "Developer", 6800)

pdt1 = pdc.PayrollDeduction("food court", "8/14/2022", 22.50, 39119)
pdt2 = pdc.PayrollDeduction("gift contribution", "8/12/2022", 25.0, 58475)
pdt3 = pdc.PayrollDeduction("food court", "8/17/2022", 15.25, 21547)
pdt4 = pdc.PayrollDeduction("vending machine", "8/22/2022", 3.00, 58475)
pdt5 = pdc.PayrollDeduction("vending machine", "8/6/2022", 2.75, 58475)

print("***Employee Pay***")
print("Name: ", employee.getname())
print("ID Number:", employee.getIDnumber())
print("Department:" ,employee.getdepartment())
print("Gross Pay:" ,employee.getmonthly_salary())

net_pay =  employee.getmonthly_salary()


pdt = [pdt1,pdt2,pdt3,pdt4,pdt5]

for record in pdt:
    if pdc.PayrollDeduction.getemployee_ID(record)==employee.getIDnumber():
        net_pay -= pdc.PayrollDeduction.getcharge_amount(record)
print("Net Pay: $",net_pay,sep="")
