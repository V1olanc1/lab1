from services.polyclinic_service import PolyclinicService
from services.file_manager import PolyclinicFileManager


class PolyclinicApp:
    """Класс приложения поликлиники с меню."""

    def __init__(self):
        self.service = None
        self.file_manager = PolyclinicFileManager()

    def display_main_menu(self):
        """Отображает главное меню."""
        print("\n" + "=" * 50)
        print("СИСТЕМА УПРАВЛЕНИЯ ПОЛИКЛИНИКОЙ")
        print("=" * 50)
        print("1. Создать новую поликлинику")
        print("2. Загрузить данные из файла")
        print("3. Сохранить данные в файл")
        print("4. Управление пациентами")
        print("5. Управление врачами")
        print("6. Управление отделениями и кабинетами")
        print("7. Управление услугами")
        print("8. Записи на прием")
        print("9. Просмотр всех данных")
        print("0. Выход")
        print("=" * 50)

    def create_new_polyclinic(self):
        """Создает новую поликлинику."""
        print("\n--- СОЗДАНИЕ НОВОЙ ПОЛИКЛИНИКИ ---")
        name = input("Введите название поликлиники: ")
        address = input("Введите адрес поликлиники: ")
        self.service = PolyclinicService(name, address)
        print(f"Создана поликлиника: {name}")

    def load_data_menu(self):
        """Меню загрузки данных."""
        print("\n--- ЗАГРУЗКА ДАННЫХ ---")
        print("1. Загрузить из JSON")
        print("2. Загрузить из XML")
        choice = input("Выберите формат: ")

        filename = input("Введите имя файла: ")
        try:
            if choice == "1":
                self.service = self.file_manager.load_from_json(filename)
            elif choice == "2":
                self.service = self.file_manager.load_from_xml(filename)
            else:
                print("Неверный выбор!")
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")

    def save_data_menu(self):
        """Меню сохранения данных."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        print("\n--- СОХРАНЕНИЕ ДАННЫХ ---")
        print("1. Сохранить в JSON")
        print("2. Сохранить в XML")
        choice = input("Выберите формат: ")

        filename = input("Введите имя файла: ")
        try:
            if choice == "1":
                self.file_manager.save_to_json(self.service, filename)
            elif choice == "2":
                self.file_manager.save_to_xml(self.service, filename)
            else:
                print("Неверный выбор!")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

    def patients_menu(self):
        """Меню управления пациентами."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- УПРАВЛЕНИЕ ПАЦИЕНТАМИ ---")
            print("1. Добавить пациента")
            print("2. Просмотреть всех пациентов")
            print("3. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.view_patients()
            elif choice == "3":
                break
            else:
                print("Неверный выбор!")

    def add_patient(self):
        """Добавляет нового пациента."""
        print("\n--- ДОБАВЛЕНИЕ ПАЦИЕНТА ---")
        first_name = input("Имя: ")
        last_name = input("Фамилия: ")
        birth_date = input("Дата рождения (ГГГГ-ММ-ДД): ")
        phone = input("Телефон: ")
        insurance_number = input("Номер страховки: ")

        try:
            patient = self.service.create_patient(
                first_name, last_name, birth_date, phone, insurance_number
            )
            print(f"Пациент добавлен: {patient}")
        except Exception as e:
            print(f"шибка при добавлении пациента: {e}")

    def view_patients(self):
        """Просматривает всех пациентов."""
        patients = self.service.get_all_patients()
        if not patients:
            print("Пациенты не найдены")
            return

        print("\n--- СПИСОК ПАЦИЕНТОВ ---")
        for i, patient in enumerate(patients, 1):
            print(f"{i}. {patient} (Тел: {patient.phone}, Страховка: {patient.insurance_number})")

    def doctors_menu(self):
        """Меню управления врачами."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- УПРАВЛЕНИЕ ВРАЧАМИ ---")
            print("1. Добавить врача")
            print("2. Просмотреть всех врачей")
            print("3. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_doctor()
            elif choice == "2":
                self.view_doctors()
            elif choice == "3":
                break
            else:
                print("Неверный выбор!")

    def add_doctor(self):
        """Добавляет нового врача."""
        print("\n--- ДОБАВЛЕНИЕ ВРАЧА ---")
        first_name = input("Имя: ")
        last_name = input("Фамилия: ")
        birth_date = input("Дата рождения (ГГГГ-ММ-ДД): ")
        phone = input("Телефон: ")
        specialization = input("Специализация: ")
        license_number = input("Номер лицензии: ")

        try:
            doctor = self.service.create_doctor(
                first_name, last_name, birth_date, phone, specialization, license_number
            )
            print(f"Врач добавлен: {doctor}")
        except Exception as e:
            print(f"Ошибка при добавлении врача: {e}")

    def view_doctors(self):
        """Просматривает всех врачей."""
        doctors = self.service.get_all_doctors()
        if not doctors:
            print("Врачи не найдены")
            return

        print("\n--- СПИСОК ВРАЧЕЙ ---")
        for i, doctor in enumerate(doctors, 1):
            print(f"{i}. {doctor} (Тел: {doctor.phone}, Лицензия: {doctor.license_number})")

    def departments_menu(self):
        """Меню управления отделениями и кабинетами."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- ОТДЕЛЕНИЯ И КАБИНЕТЫ ---")
            print("1. Добавить отделение")
            print("2. Добавить кабинет")
            print("3. Просмотреть отделения")
            print("4. Просмотреть кабинеты")
            print("5. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_department()
            elif choice == "2":
                self.add_room()
            elif choice == "3":
                self.view_departments()
            elif choice == "4":
                self.view_rooms()
            elif choice == "5":
                break
            else:
                print("Неверный выбор!")

    def add_department(self):
        """Добавляет новое отделение."""
        print("\n--- ДОБАВЛЕНИЕ ОТДЕЛЕНИЯ ---")
        name = input("Название отделения: ")
        floor = int(input("Этаж: "))

        # Показываем список врачей для выбора заведующего
        doctors = self.service.get_all_doctors()
        if not doctors:
            print("Нет доступных врачей!")
            return

        print("\nДоступные врачи:")
        for i, doctor in enumerate(doctors, 1):
            print(f"{i}. {doctor}")

        try:
            doctor_choice = int(input("Выберите номер врача (заведующего): ")) - 1
            if 0 <= doctor_choice < len(doctors):
                head_doctor_id = doctors[doctor_choice].doctor_id
                department = self.service.create_department(name, floor, head_doctor_id)
                if department:
                    print(f"Отделение добавлено: {department}")
                else:
                    print("Не удалось создать отделение")
            else:
                print("Неверный выбор врача!")
        except ValueError:
            print("Введите корректный номер!")

    def add_room(self):
        """Добавляет новый кабинет."""
        print("\n--- ДОБАВЛЕНИЕ КАБИНЕТА ---")
        room_number = input("Номер кабинета: ")
        floor = int(input("Этаж: "))
        room_type = input("Тип кабинета: ")

        # Показываем список отделений
        departments = self.service.departments
        if not departments:
            print("Нет доступных отделений!")
            return

        print("\nДоступные отделения:")
        for i, department in enumerate(departments, 1):
            print(f"{i}. {department}")

        try:
            dept_choice = int(input("Выберите номер отделения: ")) - 1
            if 0 <= dept_choice < len(departments):
                department_id = departments[dept_choice].department_id
                room = self.service.create_room(room_number, floor, room_type, department_id)
                if room:
                    print(f"Кабинет добавлен: {room}")
                else:
                    print("Не удалось создать кабинет")
            else:
                print("Неверный выбор отделения!")
        except ValueError:
            print("Введите корректный номер!")

    def view_departments(self):
        """Просматривает все отделения."""
        departments = self.service.departments
        if not departments:
            print("📝 Отделения не найдены")
            return

        print("\n--- СПИСОК ОТДЕЛЕНИЙ ---")
        for i, department in enumerate(departments, 1):
            print(f"{i}. {department} (Заведующий: {department.head_doctor.get_full_name()})")

    def view_rooms(self):
        """Просматривает все кабинеты."""
        rooms = self.service.rooms
        if not rooms:
            print("📝 Кабинеты не найдены")
            return

        print("\n--- СПИСОК КАБИНЕТОВ ---")
        for i, room in enumerate(rooms, 1):
            print(f"{i}. {room} (Отделение: {room.department.name})")

    def services_menu(self):
        """Меню управления услугами."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- УПРАВЛЕНИЕ УСЛУГАМИ ---")
            print("1. Добавить услугу")
            print("2. Просмотреть все услуги")
            print("3. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_service()
            elif choice == "2":
                self.view_services()
            elif choice == "3":
                break
            else:
                print("Неверный выбор!")

    def add_service(self):
        """Добавляет новую услугу."""
        print("\n--- ДОБАВЛЕНИЕ УСЛУГИ ---")
        name = input("Название услуги: ")
        description = input("Описание: ")
        cost = float(input("Стоимость: "))
        duration = int(input("Длительность (мин): "))

        try:
            service = self.service.create_service(name, description, cost, duration)
            print(f"Услуга добавлена: {service}")
        except Exception as e:
            print(f"Ошибка при добавлении услуги: {e}")

    def view_services(self):
        """Просматривает все услуги."""
        services = self.service.services
        if not services:
            print("Услуги не найдены")
            return

        print("\n--- СПИСОК УСЛУГ ---")
        for i, service in enumerate(services, 1):
            print(f"{i}. {service}")

    def appointments_menu(self):
        """Меню управления записями на прием."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- ЗАПИСИ НА ПРИЕМ ---")
            print("1. Создать запись")
            print("2. Просмотреть все записи")
            print("3. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.create_appointment()
            elif choice == "2":
                self.view_appointments()
            elif choice == "3":
                break
            else:
                print("Неверный выбор!")

    def create_appointment(self):
        """Создает новую запись на прием."""
        print("\n--- СОЗДАНИЕ ЗАПИСИ НА ПРИЕМ ---")

        # Выбор пациента
        patients = self.service.get_all_patients()
        if not patients:
            print("Нет доступных пациентов!")
            return
        print("\nДоступные пациенты:")
        for i, patient in enumerate(patients, 1):
            print(f"{i}. {patient}")
        patient_choice = int(input("Выберите номер пациента: ")) - 1

        # Выбор врача
        doctors = self.service.get_all_doctors()
        if not doctors:
            print("Нет доступных врачей!")
            return
        print("\nДоступные врачи:")
        for i, doctor in enumerate(doctors, 1):
            print(f"{i}. {doctor}")
        doctor_choice = int(input("Выберите номер врача: ")) - 1

        # Выбор кабинета
        rooms = self.service.rooms
        if not rooms:
            print("Нет доступных кабинетов!")
            return
        print("\nДоступные кабинеты:")
        for i, room in enumerate(rooms, 1):
            print(f"{i}. {room}")
        room_choice = int(input("Выберите номер кабинета: ")) - 1

        # Выбор услуги
        services = self.service.services
        if not services:
            print("Нет доступных услуг!")
            return
        print("\nДоступные услуги:")
        for i, service in enumerate(services, 1):
            print(f"{i}. {service}")
        service_choice = int(input("Выберите номер услуги: ")) - 1

        # Дополнительная информация
        date = input("Дата приема (ГГГГ-ММ-ДД): ")
        time = input("Время приема (ЧЧ:ММ): ")
        reason = input("Причина визита: ")

        try:
            if (0 <= patient_choice < len(patients) and
                    0 <= doctor_choice < len(doctors) and
                    0 <= room_choice < len(rooms) and
                    0 <= service_choice < len(services)):

                appointment = self.service.create_appointment(
                    patients[patient_choice].patient_id,
                    doctors[doctor_choice].doctor_id,
                    rooms[room_choice].room_id,
                    date, time,
                    services[service_choice].service_id,
                    reason
                )
                print(f"Запись создана: {appointment}")
            else:
                print("Неверный выбор!")
        except Exception as e:
            print(f"Ошибка при создании записи: {e}")

    def view_appointments(self):
        """Просматривает все записи на прием."""
        appointments = self.service.get_all_appointments()
        if not appointments:
            print("Записи не найдены")
            return

        print("\n--- СПИСОК ЗАПИСЕЙ ---")
        for i, appointment in enumerate(appointments, 1):
            print(f"{i}. {appointment}")

    def view_all_data(self):
        """Просматривает все данные поликлиники."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        print("\n" + "=" * 50)
        print("ВСЕ ДАННЫЕ ПОЛИКЛИНИКИ")
        print("=" * 50)

        print(f"\n Поликлиника: {self.service.name}")
        print(f" Адрес: {self.service.address}")

        self.view_patients()
        self.view_doctors()
        self.view_departments()
        self.view_rooms()
        self.view_services()
        self.view_appointments()

    def run(self):
        """Запускает главный цикл приложения."""
        print("Запуск системы управления поликлиникой")

        while True:
            self.display_main_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                self.create_new_polyclinic()
            elif choice == "2":
                self.load_data_menu()
            elif choice == "3":
                self.save_data_menu()
            elif choice == "4":
                self.patients_menu()
            elif choice == "5":
                self.doctors_menu()
            elif choice == "6":
                self.departments_menu()
            elif choice == "7":
                self.services_menu()
            elif choice == "8":
                self.appointments_menu()
            elif choice == "9":
                self.view_all_data()
            elif choice == "0":
                print("👋 До свидания!")
                break
            else:
                print("Неверный выбор! Попробуйте снова.")


def main():
    """Основная функция для демонстрации работы системы."""
    app = PolyclinicApp()
    app.run()


if __name__ == "__main__":
    main()