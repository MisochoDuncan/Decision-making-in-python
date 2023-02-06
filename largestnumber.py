#program to print the largest number
num1=int(input("Enter your first number :"))
num2=int(input("Enter your second number :"))
num3=int(input("Enter your third number :"))
if((num1>num2)and(num1>num3)):
    print("The first number is the largest which is =",num1)
elif((num2>num1)and(num2>num3)):
    print("The second number is the largest which is =", num2)
else:
    print("The third number is the largest which is =", num3)