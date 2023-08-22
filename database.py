# файл для работы в базой данных
import sqlite3
import json


def load_data(filename: str) -> dict:
    """
    This is a function for reading sql queries
    :param filename:
    :return queries:

    """
    with open(filename, 'r', encoding='utf-8') as f:
        queries = json.load(f)
    return queries


file = load_data('queries.json')


def create_db(dbname: str) -> None:
    """
    This is the database creation function
    :param dbname:
    :param filename:
    :return None:

    """
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute(file["create"])
    conn.commit()


def add_item(new_item: dict, dbname: str) -> None:
    """
    This is the function of adding a new entry to the phone book
    :param new_item:
    :param dbname:
    :param filename:
    :return None:

    """

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(file['add_item'], (
        new_item['last_name'], new_item['first_name'], new_item['patronymic'],
        new_item['organization'],
        new_item['work_phone'], new_item['personal_phone']))
    conn.commit()
    conn.close()


def edit_record(last_name, first_name, patronymic,
                organization, work_phone, personal_phone, dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    cursor.execute(file["edit_record"],
                   (last_name, first_name, patronymic, organization,
                    work_phone, personal_phone, last_name, first_name,
                    patronymic))

    conn.commit()
    conn.close()


def display_records(page_num, page_size, dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    offset = (page_num - 1) * page_size
    cursor.execute(file["display_records"], (page_size, offset))

    records = cursor.fetchall()
    for record in records:
        print(record)

    conn.close()


display_records(1, 3, 'phonebook.db')
