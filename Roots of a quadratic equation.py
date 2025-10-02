import math
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
D=(b*b)-(4*a*c)
if D>=0:
    r1=(-b + math.sqrt(D))/(2*a)
    r2=(-b - math.sqrt(D))/(2*a)
    print("The roots are real")
    print("r1 =",r1)
    print("r2 =",r2)
else:
    rp=-b/(2*a)
    ip= math.sqrt(-D)/(2*a)
    print("The roots are complex")
    print("r1 =",rp,"+",(ip),"j")
    print("r2 =",rp,"-",(ip),"j")
    
