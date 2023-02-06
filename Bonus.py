#program to offer bonuses to employees
salary=float(input("Enter your salary :"))
yr=int(input("Enter your years of service :"))
if(yr>10):
    bonus1=salary*0.1
    print("Your net bonus is =",bonus1)
elif((yr>=6)and (yr<=10)):
    bonus2 =salary * 0.08
    print("Your net bonus is =",bonus2)
else:
    bonus3 =salary * 0.05
    print("Your net bonus is =",bonus3)