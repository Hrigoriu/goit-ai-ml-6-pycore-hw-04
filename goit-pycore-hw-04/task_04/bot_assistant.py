def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Розділяє введений рядок на команду та аргументи."""
    parts = user_input.split() # Розбиваємо рядок за пробілами на список слів.
    # Н-д,  ("add", ["John", "123456"])
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    return command, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Додає контакт або оновлює номер, якщо ім'я вже існує."""
    if len(args) != 2:
        return "Invalid arguments. Usage: add [name] [phone]"

    name, phone = args # Додаємо контакт як словник, де ключ - ім'я, а значення - номер телефону.
    contacts[name] = phone

    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Змінює номер телефону наявного контакту."""
    if len(args) != 2:
        return "Invalid arguments. Usage: change [name] [phone]"

    name, phone = args

    # Шукаємо ім'я без урахування регістру.
    contact_name = next(
        (saved_name for saved_name in contacts if saved_name.casefold() == name.casefold()),
        None,
    )

    if contact_name is None:
        return "Contact not found."

    contacts[contact_name] = phone

    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Повертає номер телефону за ім'ям контакту."""
    if len(args) != 1:
        return "Invalid arguments. Usage: phone [name]"

    name = args[0]

    # Пошук імені також не залежить від регістру.
    for saved_name, phone in contacts.items():
        if saved_name.casefold() == name.casefold():
            return phone

    return "Contact not found."


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