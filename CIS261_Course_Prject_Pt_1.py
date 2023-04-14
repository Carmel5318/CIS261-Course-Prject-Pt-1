#Niki Decker
#CIS 261
#Course Pro Project Part 1


def Get_Employee_Name():
    employee_name = input("Enter employee name (type 'end' to quit): ")
    return employee_name

#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))

#write the Get_Hours_Worked function
def Get_Hours_Worked():
 hours_worked = float(input("Enter number of hours worked: "))
 return hours_worked

#write the Get_Hourly_Rate function
def Get_Hourly_Rate():
 hourly_rate = float(input("Enter hourly rate: "))
 return hourly_rate

# write the Get_Tax_Rate function
def Get_Tax_Rate():
 tax_rate = float(input("Enter tax rate as a decimal (e.g. 0.25 for 25%): "))
 return tax_rate



def Calculate_Tax_And_Net_Pay(hours_worked, hourly_rate, tax_rate):
    gross_pay = hours_worked * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_information(employee_name, hours_worked, hourly_rate,gross_pay, tax_rate, income_tax, net_pay):
    print("Name:  ", employee_name) 
    print("Hours Worked: ", f"{hours_worked:,.2f}")

    # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formatting

    # taxrate needs to be formatted as percentage
    print("Hourly Rate: $", f"{hourly_rate:,.2f}")
    print("Gross Pay: $", f"{gross_pay:,.2f}")
    print("Tax Rate: ", f"{tax_rate:.2%}")
    print("Income Tax: $", f"{income_tax:,.2f}")
    print("Net Pay: $", f"{net_pay:,.2f}")
    print()

def Display_Totals(Total_Employees, Total_Hours, Total_Gross_Pay, Total_Tax, Total_Net_Pay):    
    print()
    print(f"Total Number Of Employees: {Total_Employees}")
    print(f"Total Hours Worked: {Total_Hours:,.2f}")

    # write the code to print  Total_Gross_Pay, Total_Tax, and Total_Net_pay with 2 decimal places
    print(f"Total Gross Pay: ${Total_Gross_Pay:,.2f}")
    print(f"Total Tax: ${Total_Tax:,.2f}")
    print(f"Total Net Pay: ${Total_Net_Pay:,.2f}")


if __name__ == "__main__":
    Total_Employees = 0
    Total_Hours = 0.00
    Total_Gross_Pay = 0.00
    Total_Tax = 0.00
    Total_Net_Pay = 0.00
    while True:
        Employee_name = Get_Employee_Name()
        if (Employee_name.upper() == "END"):
            break

        # write the code to assign to hours the return value from Get_Hours_Worked
        hours_worked = Get_Hours_Worked()

        # write the code to assign to hourlyrate the return value from Get_Hourly_Rate
        hourly_rate = Get_Hourly_Rate()  
        
        # write the code to assign to taxrate the return value from Get_Tax_Rate
        tax_rate = Get_Tax_Rate()

        gross_pay, income_tax, net_pay = Calculate_Tax_And_Net_Pay(hours_worked, hourly_rate, tax_rate)
        display_information(Employee_name, hours_worked, hourly_rate, gross_pay, tax_rate, income_tax, net_pay)
        Total_Employees += 1
        Total_Hours += hours_worked

        # write the code to increment the other total variables with the appropriate values
        Total_Gross_Pay += gross_pay
        Total_Tax += income_tax
        Total_Net_Pay += net_pay



    Display_Totals (Total_Employees, Total_Hours, Total_Gross_Pay, Total_Tax, Total_Net_Pay)
