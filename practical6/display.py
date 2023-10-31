from MyPackage import calculator,greeting
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
print("Addition:",calculator.add(a,b))
print("Substraction:",calculator.sub(a,b))
print("Division:",calculator.div(a,b))
print("Multiplication:",calculator.mul(a,b))
name=input("Enter name: ")
greeting.sayHello(name)
