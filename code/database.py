# файл для работы в базой даннcых
import sqlite3
from func import load_queries

phrases = load_queries('data/phrases.json')


def create_db(dbname: str, file: dict) -> None:
    """
    This function creates a database
    :param dbname:
    :param file:
    :return:
    """

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute(file["create"])
    conn.commit()


def add_contact(new_item: dict, dbname: str, file: dict) -> None:
    """
    This function adds a new contact to the database.
    There is also a restriction on the uniqueness of the first name,
    last name and patronymic together.
    :param new_item:
    :param dbname:
    :param file:
    :return:
    """

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(file['add_contact'], (
        new_item['last_name'], new_item['first_name'], new_item['patronymic'],
        new_item['organization'],
        new_item['work_phone'], new_item['personal_phone']))
    conn.commit()
    conn.close()


def edit_contact(old_last_name: str, old_first_name: str,
                 old_patronymic: str, last_name: str, first_name: str,
                 patronymic: str, organization: str, work_phone: str,
                 personal_phone: str, dbname: str, file: dict) -> None:
    """
    This function changes the contact in the database
    :param old_last_name:
    :param old_first_name:
    :param old_patronymic:
    :param last_name:
    :param first_name:
    :param patronymic:
    :param organization:
    :param work_phone:
    :param personal_phone:
    :param dbname:
    :param file:
    :return:
    """

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    cursor.execute(file['edit_contact'],
                   (last_name, first_name, patronymic, organization,
                    work_phone, personal_phone, old_last_name, old_first_name,
                    old_patronymic))

    conn.commit()
    conn.close()


def display_contacts(file: dict, page_num: int = 1,
                     page_size: int = 5, dbname: str = None) -> None:
    """
    This function displays contacts with a given number of entries
    and a page, by default it is the first page with five contacts
    :param file:
    :param page_num:
    :param page_size:
    :param dbname:
    :return:
    """

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    offset = (page_num - 1) * page_size
    cursor.execute(file['display_contact'], (page_size, offset))

    records = cursor.fetchall()
    if records:
        for record in records:
            print(*record)
        conn.close()
    else:
        print(phrases['errors']['empty_phonebook'])


def search_contact(file: dict, data: list, dbname: str = None) -> None:
    """
    This function finds contacts with the given last name,
    first name, or company name
    :param file:
    :param data:
    :param dbname:
    :return:
    """

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    if not any(data):
        print(phrases['errors']['enter_param'])
        return

    query = file['search']
    values = []
    if data[0]:
        query += ' last_name = ? AND'
        values.append(data[0])
    if data[1]:
        query += ' first_name = ? AND'
        values.append(data[1])
    if data[2]:
        query += ' organization = ? AND'
        values.append(data[2])

    query = query.rstrip(' AND')
    cursor.execute(query, tuple(values))
    records = cursor.fetchall()
    if records:
        print(phrases['success']['found_contacts'])
        for record in records:
            print(*record)
    else:
        print(phrases['errors']['contacts_not_found'])

    conn.close()


def drop_contact(last_name: str, first_name: str,
                 patronymic: str, dbname: str, file: dict) -> None:
    """
    This function deletes a contact by the given first name,
    last name and patronymic.
    :param last_name:
    :param first_name:
    :param patronymic:
    :param dbname:
    :param file:
    :return:
    """
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(file['delete_contact'], (last_name, first_name, patronymic))

    conn.commit()
    conn.close()
