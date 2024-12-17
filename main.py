print("Пояснение: ** это возведение первого числа в куб")
def calculate():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            op = input("Введите операцию (+, -, *, /, //, **): ")
            num2 = float(input("Введите второе число: "))

            if op == '+':
                res = num1 + num2
            elif op == '-':
                res = num1 - num2
            elif op == '*':
                res = num1 * num2
            elif op == '//':
                res = num1 // num2
            elif op == '**':
                res = num1 * num1
            elif op == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Нельзя делить на ноль!")
                res = num1 / num2
            else:
                print("Неверная операция. Введите знак из перечисленных выше и попоробуйте снова.")
                continue



            print(f"Результат: {res}")

        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите числовое значение а не букву")
        except ZeroDivisionError as e:
            print(e)

        rep = input("Хотите выполнить ещё одно вычисление? (да/нет): ").lower()
        if rep != 'да':
            break


if __name__ == "__main__":
    calculate()
