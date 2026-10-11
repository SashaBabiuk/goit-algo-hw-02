from collections import deque


def is_palindrome(text: str) -> bool:
    normalized_text = "".join(text.casefold().split())
    characters = deque(normalized_text)

    while len(characters) > 1:
        if characters.popleft() != characters.pop():
            return False

    return True


def main():
    text = input("Введіть рядок: ")

    if is_palindrome(text):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")


if __name__ == "__main__":
    main()