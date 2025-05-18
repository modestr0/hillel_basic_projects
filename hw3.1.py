num1  = float(input("Введіть перше число: "))
operators = input("Виберіть дію (+, -, *, /):")
num2 = float(input("Введіть друге число: "))

if operators == "+":
    print("Результат дії:", num1 + num2)

elif operators == "-":
    print("Результат дії:", num1 - num2)

elif operators == "*":
    print("Результат дії:", num1 * num2)

elif operators == "/":
    if  num2 == 0:
        print("Помилка ділення на нуль неможливе")
    else:
        print("Результат дії:", num1 / num2)
else:
    print("Дія неправильна, введіть одну з наведених: (+, -, *, /):  ")

