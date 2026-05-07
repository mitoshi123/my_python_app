# app.py

# 1. Твоя функція (її ми ТЕСТУЄМО)
def calculate_area(width, height): # Перевір цю назву!
    return width * height

# 2. Введення даних (його ми ХОВАЄМО від тестів)
if __name__ == "__main__":
    # Весь код з input() має бути ТУТ всередині цієї умови
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    print(f"Результат: {add(num1, num2)}")
