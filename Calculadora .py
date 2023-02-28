#description
print("welcome to my personal calculator,this is my first personal serious project\n")

print("enter two numbers and the sinal of the operation\n")

#variables
num1 = int(input("enter a first number: "))
num2 = int(input("enter a second number: "))
opera = input("enter the sinal of the operation: ")

#loops
if opera ==   ("+"):
    print(num1,"+", num2,"=", num1+num2)
elif opera == ("-" ):
    print(num1,"-",num2,"=",num1-num2)
elif opera == ("*" or "X" or "x"):
    print(num1,"*",num2,"=",num1*num2)
elif opera == ("//" or "/" or "÷"):
    print(num1,"/",num2,"=",num1//num2)
else:
    print("is not possible to do this operatio n\n")
    print("made by murillo aparecido")

