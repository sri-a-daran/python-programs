p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (in years): "))
a = p * (1 + r/100) ** t
ci = a - p
print("Compound Interest =", ci,"rupees")

