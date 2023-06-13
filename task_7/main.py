# Список перелетов
flights = [
    {
        "номер рейса": "FL001",
        "название": "Москва - Париж",
        "время вылета": "10:00",
        "цена": 1000
    },
    {
        "номер рейса": "FL002",
        "название": "Лондон - Нью-Йорк",
        "время вылета": "14:30",
        "цена": 2000
    },
    {
        "номер рейса": "FL003",
        "название": "Токио - Сидней",
        "время вылета": "19:15",
        "цена": 1500
    }
]

# Вывод списка перелетов
print("Список перелетов:")
for flight in flights:
    print(flight["номер рейса"], "-", flight["название"], "-", flight["время вылета"], "-", flight["цена"])

# Ввод номера рейса и ФИО
flight_number = input("Введите номер рейса: ")
fio = input("Введите свое ФИО: ")
#
# Поиск выбранного перелета
selected_flight = None
for flight in flights:
    if flight["номер рейса"] == flight_number:
        selected_flight = flight
        break

# Если перелет найден
if selected_flight:
    price = selected_flight["цена"]
    payment = float(input("Введите сумму оплаты: "))

    # Проверка суммы оплаты
    if payment == price:
        print("Оплата прошла успешно")
    elif payment > price:
        change = payment - price
        print("Оплата прошла успешно. Ваша сдача:", change)
    else:
        print("Недостаточно средств для оплаты")
else:
    print("Перелет с указанным номером не найден")

# Вывод информации о выбранном перелете
if selected_flight:
    print("Номер рейса:", selected_flight["номер рейса"])
    print("ФИО:", fio)
    print("Название:", selected_flight["название"])
    print("Время вылета:", selected_flight["время вылета"])


...

# Поиск выбранного перелета и проверка наличия пользователя
selected_flight = None
user_exists = False
for flight in flights:
    if flight["номер рейса"] == flight_number:
        selected_flight = flight
        user_exists = True
        break

# Если перелет найден и пользователь существует
if selected_flight and user_exists:
    price = selected_flight["цена"]
    payment = float(input("Введите сумму оплаты: "))

    # Проверка суммы оплаты
    if payment == price:
        print("Оплата прошла успешно")
    elif payment > price:
        change = payment - price
        print("Оплата прошла успешно. Ваша сдача:", change)
    else:
        print("Недостаточно средств для оплаты")
elif selected_flight and not user_exists:
    print("Пользователь с указанным номером рейса не найден")
else:
    print("Перелет с указанным номером не найден")

# ...
