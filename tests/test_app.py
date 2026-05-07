# tests/test_app.py
from app import calculate_area # Імпортуємо функцію з твого файлу

def test_positive():
    assert calculate_area(5, 4) == 20  # Перевірка: 5*4 має бути 20

def test_zero():
    assert calculate_area(10, 0) == 0  # Перевірка множення на нуль

def test_negative():
    assert calculate_area(-2, 3) == -6 # Перевірка з від'ємним числом