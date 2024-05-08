def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
print("select operation -\n" \
      "1.Addition\n" \
      "2.subtraction\n" \
      "3.multiplication\n" \
      "4.division\n")
#input
select=int(input("select operation from 1,2,3,4: "))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", sub(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", mul(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=", div(number_1, number_2))
else:
    print("Invalid Input")