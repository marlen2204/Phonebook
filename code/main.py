from database import (create_db, add_contact, edit_contact,
                      display_contacts, search_contact, load_queries)


def main(filename, dbname):
    """
    The main function in which the action selection loop is launched.
    :param filename:
    :param dbname:
    :return:
    """

    file = load_queries(filename)
    create_db(dbname, file)
    while True:
        print("\nТелефонный справочник")
        print("1. Вывести все записи")
        print("2. Добавить новую запись")
        print("3. Редактировать записи")
        print("4. Поиск записей")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_contacts(file=file, page_num=1, page_size=5, dbname=dbname)
        elif choice == "2":
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя: ')
            patronymic = input('Введите отчество: ')
            organization = input('Введите организацию: ')
            work_phone = input('Введите рабочий телефон: ')
            personal_phone = input('Введите персональный телефон: ')
            add_contact(new_item=dict(
                last_name=last_name, first_name=first_name,
                patronymic=patronymic, organization=organization,
                work_phone=work_phone,
                personal_phone=personal_phone), dbname=dbname, file=file)
        elif choice == "3":
            last_name = input('Введите искомую фамилию: ')
            first_name = input('Введите искомое имя: ')
            patronymic = input('Введите искомое отчество: ')
            new_last_name = input('Введите новую фамилию: ')
            new_first_name = input('Введите новое имя: ')
            new_patronymic = input('Введите новое отчество: ')
            new_organization = input('Введите новое название организации: ')
            new_work_numer = input('Введите новый рабочий телефон: ')
            new_personal_number = input('Введите новый личный телефон: ')
            edit_contact(
                old_last_name=last_name, old_first_name=first_name,
                old_patronymic=patronymic, last_name=new_last_name,
                first_name=new_first_name, patronymic=new_patronymic,
                organization=new_organization, work_phone=new_work_numer,
                personal_phone=new_personal_number, dbname=dbname, file=file)
        elif choice == "4":
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя: ')
            organization = input('Введите организацию: ')
            data = list(map(lambda x: None if not x else x,
                            [last_name, first_name, organization]))

            search_contact(
                file=file, data=data, dbname=dbname)
        elif choice == "0":
            break
        else:
            print("Некорректный выбор")


if __name__ == '__main__':
    main(filename='code/queries.json', dbname='phonebook.db')
