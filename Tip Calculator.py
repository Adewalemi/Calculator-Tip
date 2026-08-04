
# Online Python - IDE, Editor, Compiler, Interpret 

print ("Welcome to tip Calculator! ")

bill = input ("What was the total bill? $")
tip = input ("How much tip would you like to give? 10, 12, or 15? ")
spilt = input ("How many people to spilt the bill? ")

realTip = float (bill) * int (tip) / 100
newBill = float (bill) + realTip
newSpilt = newBill / int (spilt)

roundBill = round (newSpilt, 2)

print (f"Each person should pay: ${roundBill}")



