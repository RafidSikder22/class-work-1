print("hello world")





num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number"))
sum = num1 + num2
print("the sum is:",sum)





name=input("enter your name:Rafid")
print("Hello," + name +"!Nice to meet you." )






num =int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")






num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
if num1 > num2:
    print(f"The larger number is {num}.")
elif num2 > num1:
    print(f"The larger number is {num2}.")
else:
    print("both numbers are equal.")







num = float(input("enter the first number:"))
operation = input("enter an operation(+, -, *, /): ")
num2 = float(input("enter the second number:"))
if operation == '+':
    result = num1 + num2
    print("result:", result)
elif operation == '-':
    result = num1 - num2
    print("result:", result)
elif operation == '*':
    result = num1 * num2
    print("result:", result)
elif operation == '/':
    if num2 !=0:
        result = num1 / num2
        print("result:", result)
    else:
        print("Error: cannot divide by zero.")
else:
    print("Invalid operatio,")





for i in range(1, 11):
    print(i)






num = float(input("Enter a number:"))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")






a = input("Enter  the first value (a):")
b = input("Enter the second value (b):")
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)






celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in fahrenheit:", fahrenheit)