print('Welcome')
fTotalBill = float(input('What was the total bill?'))
iTip = int(input("tip? 10, 12 or 15"))
iPeople = int(input("People?"))

fTipPercent = iTip/100

fTotalAmount = fTotalBill + (fTotalBill*fTipPercent)

fSplit = fTotalAmount/iPeople

print(round(fSplit,2))