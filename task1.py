from itertools import count
from queue import Empty, Queue


requests = Queue()
request_numbers = count(1)


def generate_request():
    request = {"id": next(request_numbers), "description": "Заявка клієнта"}
    requests.put(request)
    print(f"Створено заявку №{request['id']}.")


def process_request():
    try:
        request = requests.get_nowait()
    except Empty:
        print("Черга заявок порожня.")
        return

    print(f"Оброблено заявку №{request['id']}.")


def main():
    print("Система обробки заявок. Натисніть Enter для наступної заявки або q для виходу.")

    while True:
        command = input("> ").strip().lower()
        if command == "q":
            print("Роботу системи завершено.")
            break

        generate_request()
        process_request()


if __name__ == "__main__":
    main()