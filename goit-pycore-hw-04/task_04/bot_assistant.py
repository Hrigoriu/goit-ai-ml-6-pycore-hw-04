def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Розділяє введений рядок на команду та аргументи."""
    parts = user_input.split() # Розбиваємо рядок за пробілами на список слів.
    # Н-д,  ("add", ["John", "123456"])
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    return command, args

def validate_contact(name: str, phone: str) -> bool:
    """Перевіряє коректність імені та номера телефону."""
    # Перевіряємо, що ім'я та номер не порожні та номер складається лише з цифр.
    return bool(name.strip()) and bool(phone.strip()) and phone.isdigit() 


def find_contact_name(name: str, contacts: dict[str, str]) -> str | None:
    """Знаходить ім'я контакту без урахування регістру."""
    for saved_name in contacts:
        # casefold() використовується для порівняння рядків без урахування регістру.
        if saved_name.casefold() == name.casefold(): 
            return saved_name

    return None

def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Додає контакт або оновлює номер, якщо ім'я вже існує."""
    if len(args) != 2:
        return "Invalid arguments. Usage: add [name] [phone]"

    # Додаємо контакт як словник, де ключ - ім'я, а значення - номер телефону.
    name, phone = args 
    if not validate_contact(name, phone):
        return "Invalid contact information."

    # Перевіряємо, чи існує контакт з таким ім'ям.
    existing_name = find_contact_name(name, contacts)

    # Якщо контакт з таким ім'ям вже існує, оновлюємо його номер телефону.
    if existing_name is not None: 
        contacts[existing_name] = phone
        return "Contact updated."

    contacts[name] = phone # Додаємо новий контакт.

    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Змінює номер телефону наявного контакту."""
    if len(args) != 2:
        return "Invalid arguments. Usage: change [name] [phone]"

    name, phone = args

    # Перевіряємо коректність введених даних.
    if not validate_contact(name, phone):
        return "Invalid name or phone number."

    # Шукаємо контакт без урахування регістру.
    existing_name = find_contact_name(name, contacts)

    # Якщо контакт не знайдено, повертаємо повідомлення про помилку.
    if existing_name is None: 
        return "Contact not found."

    contacts[existing_name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Повертає номер телефону за ім'ям контакту."""
    if len(args) != 1:
        return "Invalid arguments. Usage: phone [name]"

    name = args[0]

    # Якщо контакт знайдено, повертаємо його номер телефону, інакше повідомляємо, що контакт не знайдено.
    existing_name = find_contact_name(name, contacts) 

    # Якщо контакт не знайдено, повертаємо повідомлення про помилку.
    if existing_name is None: 
        return "Contact not found."

    return contacts[existing_name]


def show_all(contacts: dict[str, str]) -> str:
    """Повертає всі контакти у вигляді одного рядка."""
    if not contacts:
        return "No contacts saved."

    return "\n".join(
        f"{name}: {phone}" for name, phone in contacts.items()
    )


def main() -> None:
    """Керує циклом взаємодії з користувачем."""
    contacts: dict[str, str] = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello" and not args:
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all" and not args:
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()