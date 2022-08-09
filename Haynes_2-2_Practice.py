#Steven Haynes
#Ch. 2-2 Practice Status: In Progress

#IPO: Input: monthly gross and monthly deductions (1 number)
#Process: monthly gross - monthly deductions
#Output: monthly net
#Process: monthly gross * 12
#Output: annual gross
#Process: monthly net * 12
#Output: annual net

monthly_gross = float(input('What is your Gross Monthly Income? '))
monthly_deductions = float(input('What are your total Monthly Paycheck Deductions? '))

monthly_net = (monthly_gross - monthly_deductions)

print("Your Monthly Net Income is: $1358.26", format( monthly_net, ',.2f'), sep= '')

annual_gross = (monthly_gross * 12)
print('Your Annual Gross Pay is: $', format(annual_gross, ',.2f'), sep= '')

annual_net = (monthly_net * 12)
print("Your Annual Net Pay is: $", format(annual_net, ',.2f'), sep= '')
