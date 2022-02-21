# Loan Emi
pa = 10000
yr = 5
rate = 10
intr = (pa * yr * rate) / 100
total = pa + intr
print("Interest Amount =", intr, "Total Amount =",total)
emi = total / (12 * yr)
print("Monthly Emi =", emi)
