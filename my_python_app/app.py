# app.py

# 1. Логіка (те, що ми будемо тестувати)
def calculate_area(width, height):
    return width * height

# 2. Запуск (те, що бачить користувач)
if __name__ == "__main__":
    w = int(input("Ширина: "))
    h = int(input("Висота: "))
    print(f"Площа: {calculate_area(w, h)}")