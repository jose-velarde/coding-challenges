from random import randint
from faker import Faker
import pandas as pd
import datetime

fake = Faker("en_US")

with open("data\Customers.txt", "w") as f:
    for index in range(100):
        f.write(
            "({},'{}','{}','{}'),\n".format(
                index + 1,
                fake.first_name(),
                fake.last_name(),
                fake.date_between(
                    start_date=datetime.date(year=1980, month=1, day=1), end_date="+1y"
                ),
            )
        )
        print(
            "({},{},{},{}),".format(
                index + 1,
                fake.first_name(),
                fake.last_name(),
                fake.date_between(
                    start_date=datetime.date(year=1980, month=1, day=1), end_date="+20y"
                ),
            )
        )


unique_items = [
    {
        "nombre": "Asus i3",
        "descripcion": "Notebook usada",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Asus i5",
        "descripcion": "Notebook nueva",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Asus i7",
        "descripcion": "Notebook nueva",
        "precio": "140000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Asus i9",
        "descripcion": "Notebook nueva",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Asus AMD",
        "descripcion": "Notebook nueva",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Bangho i3",
        "descripcion": "Notebook usada",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Bangho i5",
        "descripcion": "Notebook nueva",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Bangho i7",
        "descripcion": "Notebook nueva",
        "precio": "130000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Bangho i9",
        "descripcion": "Notebook nueva",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Bangho AMD",
        "descripcion": "Notebook nueva",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Lenovo i3",
        "descripcion": "Notebook usada",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Lenovo i5",
        "descripcion": "Notebook nueva",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Lenovo i7",
        "descripcion": "Notebook nueva",
        "precio": "140000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Lenovo i9",
        "descripcion": "Notebook nueva",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Lenovo AMD",
        "descripcion": "Notebook nueva",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Apple i3",
        "descripcion": "Notebook usada",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Apple i5",
        "descripcion": "Notebook nueva",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Apple i7",
        "descripcion": "Notebook nueva",
        "precio": "140000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Apple i9",
        "descripcion": "Notebook nueva",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Apple AMD",
        "descripcion": "Notebook nueva",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Dell i3",
        "descripcion": "Notebook usada",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Dell i5",
        "descripcion": "Notebook nueva",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Dell i7",
        "descripcion": "Notebook nueva",
        "precio": "140000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Dell i9",
        "descripcion": "Notebook nueva",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Dell AMD",
        "descripcion": "Notebook nueva",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Notebooks",
    },
    {
        "nombre": "Samsung j2",
        "descripcion": "Celular usado",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Samsung j7",
        "descripcion": "Celular nuevo",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Samsung A1",
        "descripcion": "Celular nuevo",
        "precio": "140000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Samsung A2",
        "descripcion": "Celular nuevo",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Samsung A4",
        "descripcion": "Celular nuevo",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Motorola E7",
        "descripcion": "Celular usado",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Motorola E9",
        "descripcion": "Celular nuevo",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Motorola G7",
        "descripcion": "Celular nuevo",
        "precio": "130000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Motorola G9",
        "descripcion": "Celular nuevo",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Motorola G10",
        "descripcion": "Celular nuevo",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "LG K12",
        "descripcion": "Celular usado",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "LG K22",
        "descripcion": "Celular nuevo",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "LG K32",
        "descripcion": "Celular nuevo",
        "precio": "140000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "LG K42",
        "descripcion": "Celular nuevo",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "LG K52",
        "descripcion": "Celular nuevo",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "iPhone 7",
        "descripcion": "Celular usado",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "iPhone 8",
        "descripcion": "Celular nuevo",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "iPhone 9",
        "descripcion": "Celular nuevo",
        "precio": "140000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "iPhone 10",
        "descripcion": "Celular nuevo",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "iPhone 11",
        "descripcion": "Celular nuevo",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Xiaomi 7S",
        "descripcion": "Celular usado",
        "precio": "100000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Xiaomi 8S",
        "descripcion": "Celular nuevo",
        "precio": "120000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Xiaomi 9S",
        "descripcion": "Celular nuevo",
        "precio": "140000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Xiaomi 10S",
        "descripcion": "Celular nuevo",
        "precio": "160000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
    {
        "nombre": "Xiaomi 11S",
        "descripcion": "Celular nuevo",
        "precio": "180000",
        "fecha_baja": "2021-12-31",
        "categoria": "Celulares",
    },
]

with open("data\Items.txt", "w") as f:
    for index, item in enumerate(unique_items):
        f.write(
            "({},'{}','{}',{},'{}','{}'),\n".format(
                index + 1,
                item["nombre"],
                item["descripcion"],
                item["precio"],
                item["fecha_baja"],
                item["categoria"],
            )
        )
        print(
            "({},{},{},{},{}'{}'),".format(
                index + 1,
                item["nombre"],
                item["descripcion"],
                item["precio"],
                item["fecha_baja"],
                item["categoria"],
            )
        )

unique_categories = ["Celulares", "Notebooks"]

with open("data\Categories.txt", "w") as f:
    for index, item in enumerate(unique_categories):
        f.write(
            "({},'{}'),\n".format(
                index + 1,
                item,
            )
        )
        print(
            "({},{}),".format(
                index + 1,
                item,
            )
        )

with open("data\Orders.txt", "w") as f:
    for index in range(300):
        customer_id = randint(1, 40)
        item_id = randint(1, 50)
        f.write(
            "({},{},'{}'),\n".format(
                index + 1,
                customer_id,
                fake.date_between(
                    start_date=datetime.date(year=2020, month=1, day=1), end_date="+1y"
                ),
            )
        )
        print(
            "({},{},{}),".format(
                index + 1,
                customer_id,
                fake.date_between(
                    start_date=datetime.date(year=2020, month=1, day=1), end_date="+1y"
                ),
            )
        )


with open("data\OrdersDetails.txt", "w") as f:
    for index in range(300):
        item_id = randint(1, 50)
        quantity = randint(300, 700)
        f.write(
            "({},{},{}),\n".format(
                index + 1,
                item_id,
                quantity,
            )
        )
        print(
            "({},{},{}),".format(
                index + 1,
                item_id,
                quantity,
            )
        )
