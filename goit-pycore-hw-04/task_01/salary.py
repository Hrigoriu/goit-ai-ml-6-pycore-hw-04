def total_salary(path: str) -> tuple[int, float]:
    """Обчислюємо загальну та середню зарплату розробників."""
    total = 0
    employee_count = 0

    try:
        with open(path, "r", encoding="utf-8") as file: #Відкриваємо файл
            for line in file: #Обробляємо кожен рядок
                line = line.strip() #Видаляємо пробіли

                if not line: # Пропускаємо порожні рядки
                    continue

                parts = line.split(",", maxsplit=1) #Розділяємо ім'я та зарплату
                # ["Alex Korp", "3000"]

                if len(parts) != 2 or not parts[0].strip(): # Перевіряємо формат рядка
                    print(f"Некоректний формат рядка: {line}")
                    continue

                try:
                    salary = int(parts[1]) #Перетворюємо зарплату на число
                except ValueError:
                    print(f"Некоректна зарплата: {line}")
                    continue

                total += salary #Обчислюємо суму
                employee_count += 1 

    except FileNotFoundError: # Обробка відсутнього файлу
        print(f"Файл не знайдено: {path}")
        return 0, 0.0

    if employee_count == 0: # Перевіряємо, чи є співробітники
        return 0, 0.0

    average = total / employee_count #Обчислюємо середнє
    return total, average


if __name__ == "__main__":
    total, average = total_salary("salaries.txt")
    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average:g}"
    )