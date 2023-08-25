from database import (create_db, add_contact, edit_contact,
                      display_contacts, search_contact, drop_contact)
from func import load_queries


def main(filename, dbname, filename_phrases):
    """
    The main function in which the action selection loop is launched.
    :param filename:
    :param dbname:
    :param filename_phrases:
    :return:
    """

    file = load_queries(filename)
    phrases = load_queries(filename_phrases)
    create_db(dbname, file)
    while True:
        print()
        print(phrases['menu']['header'])
        print(phrases['menu']['all_contacts'])
        print(phrases['menu']['add_contact'])
        print(phrases['menu']['edit_contact'])
        print(phrases['menu']['search'])
        print(phrases['menu']['delete'])
        print(phrases['menu']['escape'])

        choice = input(phrases['menu']['choice'])

        if choice == "1":
            display_contacts(file=file, page_num=1, page_size=5, dbname=dbname)
        elif choice == "2":
            last_name = input(phrases['add_contact']['input_ln'])
            first_name = input(phrases['add_contact']['input_fn'])
            patronymic = input(phrases['add_contact']['input_patr'])
            organization = input(phrases['add_contact']['input_org'])
            work_phone = input(phrases['add_contact']['input_wph'])
            personal_phone = input(phrases['add_contact']['input_pph'])
            add_contact(new_item=dict(
                last_name=last_name, first_name=first_name,
                patronymic=patronymic, organization=organization,
                work_phone=work_phone,
                personal_phone=personal_phone), dbname=dbname, file=file)
        elif choice == "3":
            last_name = input(phrases['edit_contact']['last_name'])
            first_name = input(phrases['edit_contact']['first_name'])
            patronymic = input(phrases['edit_contact']['patronymic'])
            new_last_name = input(phrases['edit_contact']['new_last_name'])
            new_first_name = input(phrases['edit_contact']['new_first_name'])
            new_patronymic = input(phrases['edit_contact']['new_patronymic'])
            new_organization = input(phrases['edit_contact']['new_organization'])
            new_work_numer = input(phrases['edit_contact']['new_work_numer'])
            new_personal_number = input(phrases['edit_contact']['new_personal_number'])
            edit_contact(
                old_last_name=last_name, old_first_name=first_name,
                old_patronymic=patronymic, last_name=new_last_name,
                first_name=new_first_name, patronymic=new_patronymic,
                organization=new_organization, work_phone=new_work_numer,
                personal_phone=new_personal_number, dbname=dbname, file=file)
        elif choice == "4":
            last_name = input(phrases['add_contact']['input_ln'])
            first_name = input(phrases['add_contact']['input_fn'])
            organization = input(phrases['add_contact']['input_org'])
            data = list(map(lambda x: None if not x else x,
                            [last_name, first_name, organization]))

            search_contact(
                file=file, data=data, dbname=dbname)
        elif choice == "0":
            break
        elif choice == '5':
            last_name = input(phrases['edit_contact']['last_name'])
            first_name = input(phrases['edit_contact']['first_name'])
            patronymic = input(phrases['edit_contact']['patronymic'])
            drop_contact(last_name, first_name, patronymic, dbname, file)

        else:
            print(phrases['errors']['wrong_choice'])


if __name__ == '__main__':
    main(filename='data/queries.json', dbname='phonebook.db', filename_phrases='data/phrases.json')
