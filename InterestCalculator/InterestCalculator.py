print('----- Interest Calculator -----')

principalAmount = float(input('Principal amount: '))
interest = float(input('Rate of Interest: '))
years = int(input('Duration (no. of years) ?'))

total = (principalAmount * pow(1 + (interest/100), years))
interest = total - principalAmount

print("----- Details Calculated -----")
print('\nTotal = %0.2f' %total)
print('\nInterest = %0.2f' %interest)

