unit1=int(input("Enter the marks of the first unit : "))
unit2=int(input("Enter the marks of the second unit : "))
unit3=int(input("Enter the marks of the third unit : "))
unit4=int(input("Enter the marks of the fourth unit : "))
avr = ((unit1 + unit2 + unit3 + unit4) / 4)
print("Your Total Average Marks is =",avr)
if((avr>=70)and(avr<=100)):
    print("Your Grade is A")
elif((avr>=60)and(avr<=69)):
    print("Your Grade is B")
elif ((avr >= 50) and (avr <= 59)):
    print("Your Grade is C")
elif ((avr >= 40) and (avr <= 49)):
    print("Your Grade is D")
else:
    print("You failed the exams")