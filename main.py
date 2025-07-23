from datetime import datetime
from приложение.salary import calculate_salary
from приложение.база_данных.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f"Текущая дата: {datetime.now().date()}")