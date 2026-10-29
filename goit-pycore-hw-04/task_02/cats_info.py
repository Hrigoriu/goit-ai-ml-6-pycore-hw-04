def get_cats_info(path: str) -> list[dict[str, str]]:
    """Читає файл і повертає список словників з інформацією про котів."""
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file: # Читаємо файл
            for line in file:
                line = line.strip() # Видаляємо пробіли

                if not line: # Пропускаємо порожні рядки
                    continue

                parts = line.split(",") # Розділяємо рядок на частини за комами

                if len(parts) != 3: # Перевіряємо, чи рядок має три частини (id, name, age)
                    print(f"Некоректний формат рядка: {line}")
                    continue

                cat_id, name, age = parts # Формуємо словник з інформацією про кота

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age,
                })

    except FileNotFoundError: # Обробка відсутнього файлу
        print(f"Файл не знайдено: {path}")
        return []

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)