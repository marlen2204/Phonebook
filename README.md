# Phonebook 📞
### Тестовое задание
### Для чего проект?
Проект Phonebook создан для удобного хранения, добавления и поиска контактов.

Полный список возможностей:  
- создание справочника  
- просмотр записей с указанием количества записей на странице и номера страницы  
- добавление записей  
- редактирование записей  
- поиск по имени, фамилии или названию организации  
- удаление по имени, фамилии и отчеству  

### Как запустить?
Для начала необходимо скачать репозиторий с github:
```angular2html
git clone https://github.com/marlen2204/Phonebook
```
Для того, чтобы запустить программу, введите команду (из корневой директории проекта) :
```angular2html
# lunux и mac os
python3 code/main.py
# windows
python code/main.py
```
### Как работать с программой?
При запуске программы появляется меню:

![Alt text](/img/menu.png?raw=true "Optional Title")

Чтобы выбрать какое-либо действие, необходимо ввести нужную цифру.

> Примечания:  
1 )  поиск осуществляется хотя бы по одному из этих параметров: имя, фамилия, организация  
2 )  для того, чтобы изменить данные контакта или удалить контакт необходимо ввести все из этих параметров: имя, фамилия, отчество  
3 )  при добавлении нового контакта нужно учитывать, что в базе данных поддерживается уникальность сочетания трех полей: имени, фамилии и отчества, соответственно добавить эти абсолютно совпадающие параметры нельзя.
