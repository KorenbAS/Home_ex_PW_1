from menu import Menu
from console import *
from screen import Screen
from notes import Notes
from contacts import Contacts
from notereader import Note_reader
from contactreader import Contact_reader
from notesmanager import Notes_manager
from contactsmanager import Contacts_manager
from valuereader import Value_reader

import colorama
colorama.init(autoreset=True)


# шляхи до файлів
NOTES_FILE = 'notes.bin'
CONTACS_FILE = 'contacts.bin'

# Пункти головного меню
MAIN_MENU = [
    'Контакти',
    'Нотатки',
    'Вихід',
]
CONTACS_SUB = 0
NOTES_SUB = 1
MAIN_MENU_BREAK = 2

# Підпункти
CONTAСTS_MENU = [
    'Додати контакт',
    'Переглянути контакти',
    'Знайти контакт',
    'Назад'
]
CONTACTS_ADD = 0
CONTACTS_SHOW_ALL = 1
CONTACTS_SEARCH = 2
CONTACTS_BREAK = 3

# Підпункти
NOTES_MENU = [
    'Додати нотатку',
    'Переглянути нотатки',
    'Пошук нотатки',
    'Назад'
]
NOTES_ADD = 0
NOTES_SHOW_ALL = 1
NOTES_SEARCH = 2
NOTES_BREAK = 3


hide_cursor()

# екземпляри класів меню
main_menu = Menu(
    Screen('Персональний помічник', 'ESC - вихід | ENTER - вибір | Вверх/Вниз - навігація'), MAIN_MENU)
contacts_menu = Menu(
    Screen('Книга контактів', 'ESC - вихід | ENTER - вибір | Вверх/Вниз - навігація'), CONTAСTS_MENU)
notes_menu = Menu(
    Screen('Нотатки', 'ESC - вихід | ENTER - вибір | Вверх/Вниз - навігація'), NOTES_MENU)

# екземпляри класів сховища нотаток та контактів
my_notes = Notes(NOTES_FILE)
my_contacts = Contacts(CONTACS_FILE)

# Цикл взаємодії з користувачем
choice = Menu.NONE
while choice != Menu.BREAK:
    choice_contacts = Menu.NONE
    choice_notes = Menu.NONE

    choice = main_menu.start()
    
    # вибране підменю контакти 
    if choice == CONTACS_SUB:
        while choice_contacts != Menu.BREAK:
            choice_contacts = contacts_menu.start()
            # додати
            if choice_contacts == CONTACTS_ADD:
                # додаємо новий контакт
                contact = Contact_reader().read()
                my_contacts.add(contact)
            # пошук
            elif choice_contacts == CONTACTS_SEARCH:
                key_word = Value_reader(Screen(
                    "Введіть ключове слово для пошуку", "Слово не може бути пустим | Enter - для підтвердження"), None).read()
                Contacts_manager(my_contacts, key_word).interactive()
            # показати всі
            elif choice_contacts == CONTACTS_SHOW_ALL:
                Contacts_manager(my_contacts, None).interactive()
            # назад
            elif choice_contacts == CONTACTS_BREAK:
                break

    # вибране підменю нотатки
    elif choice == NOTES_SUB:
        while choice_notes != Menu.BREAK:
            choice_notes = notes_menu.start()
            # підменю додати
            if choice_notes == NOTES_ADD:
                # створюємо нову нотатку
                note = Note_reader(Screen("Введіть текст нової нотатки",
                                   "Enter - новий рядок. Рядки можете залишати пустими. Допустимий розмір нотатки 8 рядків по 64 букви")).read()
                my_notes.add(note)
            # показати всі
            elif choice_notes == NOTES_SHOW_ALL:
                # менеджер нотаток
                Notes_manager(my_notes, None).interactive()
            # пошук
            elif choice_notes == NOTES_SEARCH:
                tag_word = Value_reader(Screen(
                    "Введіть ключове слово для пошуку", "Слово не може бути пустим | Enter - для підтвердження"), None).read()
                Notes_manager(my_notes, tag_word).interactive()
            # назад
            elif choice_notes == NOTES_BREAK:
                break

    elif choice == MAIN_MENU_BREAK:
        break

clear_console()
show_cursor()
