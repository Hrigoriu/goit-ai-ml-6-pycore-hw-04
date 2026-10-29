import sys
from pathlib import Path

from colorama import Fore, Style, init


def display_directory_tree(directory: Path, prefix: str = "") -> None:
    """Рекурсивно виводить структуру директорії."""
    try:
        contents = sorted( # Сортуємо вміст директорії: спочатку папки, потім файли, за алфавітом
            directory.iterdir(),
            key=lambda path: (not path.is_dir(), path.name.lower()),
        )
    except OSError as error: # Обробка помилок доступу до директорії
        print(f"{prefix}┗━━ {Fore.RED}Помилка доступу: {error}{Style.RESET_ALL}")
        return

    for index, path in enumerate(contents): # Перебираємо вміст директорії
        # Формуємо гілки дерев
        is_last = index == len(contents) - 1
        pointer = "┗━━ " if is_last else "┣━━ "

        if path.is_dir(): # Якщо це директорія, виводимо її назву синім кольором
            print(f"{prefix}{pointer}{Fore.BLUE}{path.name}/{Style.RESET_ALL}")

            extension = "    " if is_last else "┃   "
            display_directory_tree(path, prefix + extension)
        else: # Якщо це файл, виводимо його назву зеленим кольором
            print(f"{prefix}{pointer}{Fore.GREEN}{path.name}{Style.RESET_ALL}")


def main() -> None:
    """Перевіряє аргумент командного рядка та запускає обхід."""
    init(autoreset=True)

    if len(sys.argv) != 2: # Перевіряємо, чи передано шлях до директорії
        # sys.argv[0] — ім'я скрипту
        # sys.argv[1] — переданий шлях
        print(f"{Fore.RED}Використання: python structure_dir.py <шлях_до_директорії>")
        sys.exit(1) # Виходимо з кодом помилки 1, якщо аргументів недостатньо

    root_path = Path(sys.argv[1]) # Створюємо об'єкт Path для переданого шляху

    if not root_path.exists(): # Перевіряємо, чи існує шлях
        print(f"{Fore.RED}Помилка: шлях '{root_path}' не існує.")
        sys.exit(1)

    if not root_path.is_dir(): # Перевіряємо, чи є шлях директорією
        print(f"{Fore.RED}Помилка: '{root_path}' не є директорією.")
        sys.exit(1)

    print(f"{Fore.CYAN}{root_path.name or root_path}{Style.RESET_ALL}") # Виводимо назву кореневої директорії
    display_directory_tree(root_path)


if __name__ == "__main__":
    main()