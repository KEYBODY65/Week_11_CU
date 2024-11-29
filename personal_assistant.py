import pandas as pd

class ManageNotes:
    def __init__(self):
        self.notes = pd.DataFrame(columns=["id", "title", "content", "timestamp"])
        self.tasks = pd.DataFrame(columns=["id", "title", "description", "done" ,"priority","due_date"])
        self.cntacts = pd.DataFrame(columns=["id", "name", "phone", "email"])
        self.finance_records = pd.DataFrame(columns=["id", "amount", "category", "date", "description"])

    def manage_notes(self):
        while True:
            print("1)Создание новой заметки")
            print("2)Просмотр списка заметок")
            print("3)Просмотр подробностей заметки")
            print("4)Редактирование заметки")
            print("5)Удаление заметки")
            print("6)Импорт заметок в формте CSV")
            print("7)Экспорт заметок в формте CSV")
            choice = input("Выш выбор: ")

            if choice == "1":
                title = input("Заголовок заметки:")
                content = input("Содежимое заметки")
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                note_data = {'title':title, 'content':content, 'timestamp':timestamp}
                self.notes.append(note_data, ignore_index=True)
                print("Заметка успешно добавлена!")
            elif choice == "2":
                if len(self.notes) == 0:
                    print("No notes found.")
                else:
                    print(self.notes)
            elif choice == "3":
                note_titile = input("Введите заголовок заметки для просмотра: ")
                print(self.notes[self.notes['title'] == note_titile])
            elif choice == "4":
                    note_title = int(input("Введите заголовок заметки для редактирования: "))
                    if note_id in self.notes:
                        title = input("Заголовок заметки:")
                        content = input("Содежимое заметки")
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        note_data = {'id': random.randint(1, 1000000), 'title':title, 'content':content, 'timestamp':timestamp}
                        self.notes.loc[self.notes['title'] == note_title] = note_data
                        print("Заметка успешно обновлена!")
                    else:
                        print("Заметка не найдена.")
            elif choice == "5":
                note_tit = int(input("Введите заголовок заметки для удаления: "))
                if note_id in self.notes:
                    self.notes = self.notes[self.notes['title'] != note_tit]
                    print("Заметка успешно удалена!")
                else:
                    print("Заметка не найдена.")
            elif choice == "6":
                try:
                    df = pd.read_csv(input('Путь до файла'))
                    print('Заметки успешно импортированы')
                except Exception:
                    print('Не удалось импортировать заметки')
            elif choice == "7":
                try:
                    df.to_json('notes.json')
                    print('Заметки успешно экспортированы')
                except Exception:
                    print('Не удалось экспортировать заметки')
            else:
                print("К сожалению такой команды нет")
    def manage_tasks(self):
        while True:
            print("1)Создание новой задачи")
            print("2)Просмотр списка задач")
            print("3)Отметка задачи как выполненной")
            print("4)Редактирование задачи")
            print("5)Удаление задачи")
            print("6)Импорт задач в формте CSV")
            print("7)Экспорт задач в формте CSV")
            choice = input("Выш выбор: ")

            if choice == '1':
                title = input("Заголовок задачи:")
                description = input("Описание задачи")
                priority = input("Приоритет задачи")
                due_date = input("Дата выполнения задачи((ДД-ММ-ГГГГ))")
                task_data = {'title':title, 'description':description, 'priority':priority, 'due_date':due_date}
                self.tasks.append(task_data, ignore_index=True)
                print("Задача успешно добавлена!")
            elif choice == '2':
                if len(self.tasks) == 0:
                    print("No tasks found.")
                else:
                    print(self.tasks)
            elif choice == '3':
                    task_tit = int(input("Введите заголовок задачи для отметки как выполненной: "))
                    if task_id in self.tasks:
                        self.tasks.loc[self.tasks['title'] == task_tit] = True
                        print("Ура! Задача выполнена!")
                    else:
                        print("Задача не найдена.")
            elif choice == '4':
                    task_titel = int(input("Введите заголовок задачи для редактирования: "))
                    if task_id in self.tasks:
                        title = input("Заголовок задачи:")
                        description = input("Описание задачи")
                        priority = input("Приоритет задачи")
                        due_date = input("Дата выполнения задачи")
                        task_data = {'id': random.randint(1, 1000000), 'title':title, 'description':description, 'priority':priority, 'due_date':due_date}
                        self.tasks.loc[self.tasks['title'] == task_titel] = task_data
                        print("Задача успешно обновлена!")
                    else:
                        print("Задача не найдена.")
            elif choice == '5':
                task_tit = int(input("Введите заголовок задачи для удаления: "))
                if task_id in self.tasks:
                    self.tasks = self.tasks[self.tasks['title'] != task_tit]
                    print("Задача успешно удалена!")
                else:
                    print("Задача не найдена.")
            elif choice == '6':
                    try:
                        df = pd.read_csv(input('Путь до файла'))
                        print('Задачи успешно импортированы')
                    except Exception:
                        print('Не удалось импортировать задачи')
            elif choice == '7':
                    try:
                        df.to_json('tasks.json')
                        print('Задачи успешно экспортированы')
                    except Exception:
                        print('Не удалось экспортировать задачи')
    def manage_contacts(self):
        while True:
            print("1)Создание нового контакта")
            print("2)Поиск контакта по имени или номеру телефона")
            print("3)Редактирование контакта")
            print("4)Удаление контакта")
            print("5)Импорт контактов в формте CSV")
            print("6)Экспорт контактов в формте CSV")
            choice = input("Выш выбор: ")
            if choice == '1':
                name = input("Введите имя контакта: ")
                phone = input("Введите номер телефона: ")
                email = input("Введите адрес электронной почты: ")
                contact_data = {'name': name, 'phone': phone, 'email': email}
                self.contacts.append(contact_data, ignore_index=True)
                print("Контакт успешно добавлен!")
            elif choice == '2':
                search_term = input("Введите имя или номер телефона для поиска: ")
                if search_term in self.contacts['name'] or search_term in self.contacts['phone']:
                    results = self.contacts[self.contacts['name'].str.contains(search_term, case=False) or self.contacts['phone'].str.contains(search_term, case=False)] # условие для поиска по номеру или почте
                    print(results)
                else:
                    print("Контакт не найден.")
            elif choice == '3':
                contact_id = int(input("Введите имя контакта для редактирования: "))
                if contact_id in self.contacts:
                    name = input("Введите новое имя контакта: ")
                    phone = input("Введите новый номер телефона: ")
                    email = input("Введите новый адрес электронной почты: ")
                    contact_data = {'id': contact_id, 'name': name, 'phone': phone, 'email': email}
                    self.contacts.loc[self.contacts['id'] == contact_id] = contact_data
                    print("Контакт успешно обновлен!")
                else:
                    print("Контакт не найден.")
            elif choice == '4':
                contact_id = int(input("Введите имя контакта для удаления: "))
                if contact_id in self.contacts:
                    self.contacts = self.contacts[self.contacts['id'] != contact_id]
                    print("Контакт успешно удален!")
                else:
                    print("Контакт не найден.")
            elif choice == '5':
                try:
                    df = pd.read_csv(input('Путь до файла'))
                    print('Контакты успешно импортированы')
                except Exception:
                    print('Не удалось импортировать контакты')
            elif choice == '6':
                try:
                    df.to_json('contacts.json')
                    print('Контакты успешно экспортированы')
                except Exception:
                    print('Не удалось экспортировать контакты')
    def manage_financerecords(self):
        while True:
            print("1)Добавить финансовую запись")
            print("2)просмотр всех финансвовых записок")
            print("3)Генерация отчётов о финансовой активности за поределённый период")
            print("4)Импорт финансовых записей в формте CSV")
            print("5)Экспорт финансовых записей в формте CSV")
            choice = input("Выш выбор: ")
            if choice == '1':
                amount = input("Введите сумму финансовой записи: ")
                category = input("Введите категорию финансовой записи: ")
                date = input("Введите дату финансовой записи: ")
                description = input("Введите описание финансовой записи: ")
                finance_data = {'date': date, 'category': category, 'amount': amount, 'description': description}
                self.finance_records.append(finance_data, ignore_index=True)
                print("Финансовая запись успешно добавлена")
            elif choice == '2':
                    date_or_cat = input("Введите дату или категорию для поиска: ")
                    if date_or_cat in self.finance_records['date'] or date_or_cat in self.finance_records['category']:
                        results = self.finance_records[self.finance_records['date'].str.contains(date_or_cat, case=False) or self.finance_records['category'].str.contains(date_or_cat, case=False)]
                        print(results)
                    else:
                        print("Финансовая запись не найдена.")
            elif choice == '3':
                start_date = input("Введите начальную дату: ")
                end_date = input("Введите конечную дату: ")
                results = self.finance_records[(self.finance_records['date'] >= start_date) & (self.finance_records['date'] <= end_date)]
                print(results)
            elif choice == '4':
                try:
                    df = pd.read_csv(input('Путь до файла'))
                    print('Финансовые записи успешно импортированы')
                except Exception:
                    print('Не удалось импортировать финансовые записи')
            elif choice == '5':
                try:
                    df.to_json('finance.json')
                    print('Финансовые записи успешно экспортированы')
                except Exception:
                    print("Не удалось экспортировать финансовые записи")
    def calculator(num1, num2, operation):

        try:
            if operation == 'add':
                return num1 + num2
            elif operation == 'subtract':
                return num1 - num2
            elif operation == 'multiply':
                return num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    raise ValueError("Ошибка: Деление на ноль!")
                return num1 / num2
            else:
                raise ValueError("Ошибка: Неверная операция. Используйте 'add', 'subtract', 'multiply' или 'divide'.")
        except Exception as e:
            return str(e)
            

def main():
    manager = ManageNotes()
    print("Добро пожаловать в Персональный помощник!")
    while True:
        print("Выберите действие:")
        print("1) Управление заметками")
        print("2) Управление задачами")
        print("3) Управление контактами")
        print("4) Управление финансовыми записями")
        print("5) Калькулятор")
        print("6) Выход")
        choice = input("Ваш выбор: ")
        if choice == '1':
            manager.manage_notes()
        elif choice == '2':
            manager.manage_tasks()
        elif choice == '3':
            manager.manage_contacts()
        elif choice == '4':
            manager.manage_finance_records()
        elif choice == '5':
            manager.manage_finance_records()
        elif choice == '6':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
