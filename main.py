import re
from datetime import datetime
from services.polyclinic_service import PolyclinicService
from services.file_manager import PolyclinicFileManager


class Validator:
    """Класс для валидации вводимых данных."""

    @staticmethod
    def validate_name(name: str, field_name: str) -> bool:
        """Проверяет имя/фамилию/название."""
        if not name or len(name.strip()) < 2:
            print(f"{field_name} должно содержать минимум 2 символа")
            return False
        if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\s\-]+$', name):
            print(f"{field_name} может содержать только буквы, пробелы и дефисы")
            return False
        return True

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Проверяет номер телефона."""
        # Убираем все нецифровые символы кроме +
        cleaned_phone = re.sub(r'[^\d+]', '', phone)

        # Проверяем российские форматы: +7..., 8..., 7...
        if (cleaned_phone.startswith('+7') and len(cleaned_phone) == 12) or \
                (cleaned_phone.startswith('8') and len(cleaned_phone) == 11) or \
                (cleaned_phone.startswith('7') and len(cleaned_phone) == 11):
            return True

        print("Неверный формат телефона. Используйте: +7XXX..., 8XXX... или 7XXX... (10 цифр после кода)")
        return False

    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Проверяет дату в формате ГГГГ-ММ-ДД."""
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            # Проверяем, что дата не в будущем (для даты рождения)
            if date > datetime.now():
                print("Дата не может быть в будущем")
                return False
            # Проверяем разумный возраст (не старше 150 лет)
            if (datetime.now() - date).days > 150 * 365:
                print("Неверная дата рождения")
                return False
            return True
        except ValueError:
            print("Неверный формат даты. Используйте: ГГГГ-ММ-ДД")
            return False

    @staticmethod
    def validate_insurance_number(number: str) -> bool:
        """Проверяет номер страховки - только 16 цифр."""
        if not number:
            print("❌ Номер страховки не может быть пустым")
            return False
        if len(number) != 16:
            print("❌ Номер страховки должен содержать ровно 16 цифр")
            return False
        if not number.isdigit():
            print("❌ Номер страховки должен содержать только цифры")
            return False
        return True

    @staticmethod
    def validate_license_number(number: str) -> bool:
        """Проверяет номер лицензии врача."""
        if not number or len(number.strip()) < 5:
            print("Номер лицензии должен содержать минимум 5 символов")
            return False
        if not re.match(r'^[a-zA-Zа-яА-ЯёЁ0-9\-]+$', number):
            print("Номер лицензии может содержать только буквы, цифры и дефисы")
            return False
        return True

    @staticmethod
    def validate_specialization(spec: str) -> bool:
        """Проверяет специализацию врача."""
        if not spec or len(spec.strip()) < 3:
            print("Специализация должна содержать минимум 3 символа")
            return False
        if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\s\-]+$', spec):
            print("Специализация может содержать только буквы, пробелы и дефисы")
            return False
        return True

    @staticmethod
    def validate_floor(floor: str) -> bool:
        """Проверяет номер этажа."""
        try:
            floor_num = int(floor)
            if 1 <= floor_num <= 50:  # Разумные пределы для этажей
                return True
            else:
                print("Этаж должен быть от 1 до 50")
                return False
        except ValueError:
            print("Этаж должен быть числом")
            return False

    @staticmethod
    def validate_room_number(number: str) -> bool:
        """Проверяет номер кабинета."""
        if not number or len(number.strip()) < 1:
            print("Номер кабинета не может быть пустым")
            return False
        if not re.match(r'^[a-zA-Zа-яА-ЯёЁ0-9\-\s]+$', number):
            print("Номер кабинета может содержать только буквы, цифры, пробелы и дефисы")
            return False
        return True

    @staticmethod
    def validate_room_type(room_type: str) -> bool:
        """Проверяет тип кабинета."""
        valid_types = ['examination', 'procedure', 'surgery', 'consultation', 'other']
        if room_type.lower() not in valid_types:
            print(f"Неверный тип кабинета. Допустимые: {', '.join(valid_types)}")
            return False
        return True

    @staticmethod
    def validate_cost(cost: str) -> bool:
        """Проверяет стоимость."""
        try:
            cost_num = float(cost)
            if cost_num >= 0:
                return True
            else:
                print("Стоимость не может быть отрицательной")
                return False
        except ValueError:
            print("Стоимость должна быть числом")
            return False

    @staticmethod
    def validate_duration(duration: str) -> bool:
        """Проверяет длительность в минутах."""
        try:
            duration_num = int(duration)
            if 1 <= duration_num <= 480:  # От 1 минуты до 8 часов
                return True
            else:
                print("Длительность должна быть от 1 до 480 минут")
                return False
        except ValueError:
            print("Длительность должна быть целым числом")
            return False

    @staticmethod
    def validate_appointment_date(date_str: str) -> bool:
        """Проверяет дату приема."""
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            if date < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
                print("Дата приема не может быть в прошлом")
                return False
            return True
        except ValueError:
            print("Неверный формат даты. Используйте: ГГГГ-ММ-ДД")
            return False

    @staticmethod
    def validate_appointment_time(time_str: str) -> bool:
        """Проверяет время приема."""
        try:
            time = datetime.strptime(time_str, '%H:%M')
            hour = time.hour
            if 8 <= hour <= 20:  # Рабочее время с 8:00 до 20:00
                return True
            else:
                print("Время приема должно быть с 8:00 до 20:00")
                return False
        except ValueError:
            print("Неверный формат времени. Используйте: ЧЧ:ММ")
            return False

    @staticmethod
    def validate_reason(reason: str) -> bool:
        """Проверяет причину визита."""
        if not reason or len(reason.strip()) < 5:
            print("Причина визита должна содержать минимум 5 символов")
            return False
        return True


class PolyclinicApp:
    """Класс приложения поликлиники с меню."""

    def __init__(self):
        self.service = None
        self.file_manager = PolyclinicFileManager()
        self.validator = Validator()

    def get_valid_input(self, prompt: str, validation_func, field_name: str = "", max_attempts: int = 3):
        """Получает валидный ввод от пользователя."""
        attempts = 0
        while attempts < max_attempts:
            value = input(prompt).strip()
            if validation_func(value, field_name) if field_name else validation_func(value):
                return value
            attempts += 1
            print(f"Попытка {attempts}/{max_attempts}")

        print("Превышено максимальное количество попыток. Возврат в меню.")
        return None

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
        name = input("Введите название поликлиники: ").strip()
        if not name:
            print("Название поликлиники не может быть пустым")
            return

        address = input("Введите адрес поликлиники: ").strip()
        if not address:
            print("Адрес не может быть пустым")
            return

        self.service = PolyclinicService(name, address)
        print(f"Создана поликлиника: {name}")

    def load_data_menu(self):
        print("\n--- ЗАГРУЗКА ДАННЫХ ---")
        print("1. Загрузить из JSON")
        print("2. Загрузить из XML")
        choice = input("Выберите формат: ").strip()
        filename = input("Введите имя файла: ").strip()
        if not filename:
            print("Имя файла не может быть пустым")
            return

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
        choice = input("Выберите формат: ").strip()

        filename = input("Введите имя файла: ").strip()
        if not filename:
            print("Имя файла не может быть пустым")
            return

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
            choice = input("Выберите действие: ").strip()

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

        first_name = self.get_valid_input("Имя: ", self.validator.validate_name, "Имя")
        if not first_name: return

        last_name = self.get_valid_input("Фамилия: ", self.validator.validate_name, "Фамилия")
        if not last_name: return

        birth_date = self.get_valid_input("Дата рождения (ГГГГ-ММ-ДД): ", self.validator.validate_date)
        if not birth_date: return

        phone = self.get_valid_input("Телефон: ", self.validator.validate_phone)
        if not phone: return

        insurance_number = self.get_valid_input("Номер страховки: ", self.validator.validate_insurance_number)
        if not insurance_number: return

        try:
            patient = self.service.create_patient(
                first_name, last_name, birth_date, phone, insurance_number
            )
            print(f"Пациент добавлен: {patient}")
        except Exception as e:
            print(f"Ошибка при добавлении пациента: {e}")

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
            choice = input("Выберите действие: ").strip()

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

        first_name = self.get_valid_input("Имя: ", self.validator.validate_name, "Имя")
        if not first_name: return

        last_name = self.get_valid_input("Фамилия: ", self.validator.validate_name, "Фамилия")
        if not last_name: return

        birth_date = self.get_valid_input("Дата рождения (ГГГГ-ММ-ДД): ", self.validator.validate_date)
        if not birth_date: return

        phone = self.get_valid_input("Телефон: ", self.validator.validate_phone)
        if not phone: return

        specialization = self.get_valid_input("Специализация: ", self.validator.validate_specialization)
        if not specialization: return

        license_number = self.get_valid_input("Номер лицензии: ", self.validator.validate_license_number)
        if not license_number: return

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
            choice = input("Выберите действие: ").strip()

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

        name = self.get_valid_input("Название отделения: ", self.validator.validate_name, "Название отделения")
        if not name: return

        floor = self.get_valid_input("Этаж: ", self.validator.validate_floor)
        if not floor: return

        # Показываем список врачей для выбора заведующего
        doctors = self.service.get_all_doctors()
        if not doctors:
            print("Нет доступных врачей!")
            return

        print("\nДоступные врачи:")
        for i, doctor in enumerate(doctors, 1):
            print(f"{i}. {doctor}")

        try:
            doctor_choice = input("Выберите номер врача (заведующего): ").strip()
            if not doctor_choice.isdigit():
                print("Введите номер!")
                return

            doctor_choice = int(doctor_choice) - 1
            if 0 <= doctor_choice < len(doctors):
                head_doctor_id = doctors[doctor_choice].doctor_id
                department = self.service.create_department(name, int(floor), head_doctor_id)
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

        room_number = self.get_valid_input("Номер кабинета: ", self.validator.validate_room_number)
        if not room_number: return

        floor = self.get_valid_input("Этаж: ", self.validator.validate_floor)
        if not floor: return

        room_type = self.get_valid_input("Тип кабинета (examination/procedure/surgery/consultation/other): ",
                                         self.validator.validate_room_type)
        if not room_type: return

        # Показываем список отделений
        departments = self.service.departments
        if not departments:
            print("Нет доступных отделений!")
            return

        print("\nДоступные отделения:")
        for i, department in enumerate(departments, 1):
            print(f"{i}. {department}")

        try:
            dept_choice = input("Выберите номер отделения: ").strip()
            if not dept_choice.isdigit():
                print("Введите номер!")
                return

            dept_choice = int(dept_choice) - 1
            if 0 <= dept_choice < len(departments):
                department_id = departments[dept_choice].department_id
                room = self.service.create_room(room_number, int(floor), room_type, department_id)
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
            print("Отделения не найдены")
            return

        print("\n--- СПИСОК ОТДЕЛЕНИЙ ---")
        for i, department in enumerate(departments, 1):
            print(f"{i}. {department} (Заведующий: {department.head_doctor.get_full_name()})")

    def view_rooms(self):
        """Просматривает все кабинеты."""
        rooms = self.service.rooms
        if not rooms:
            print("Кабинеты не найдены")
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
            choice = input("Выберите действие: ").strip()

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

        name = input("Название услуги: ").strip()
        if not name:
            print("Название услуги не может быть пустым")
            return

        description = input("Описание: ").strip()
        if not description:
            print("Описание не может быть пустым")
            return

        cost = self.get_valid_input("Стоимость: ", self.validator.validate_cost)
        if not cost: return

        duration = self.get_valid_input("Длительность (мин): ", self.validator.validate_duration)
        if not duration: return

        try:
            service = self.service.create_service(name, description, float(cost), int(duration))
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
            choice = input("Выберите действие: ").strip()

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

        patient_choice = input("Выберите номер пациента: ").strip()
        if not patient_choice.isdigit():
            print("Введите номер!")
            return

        # Выбор врача
        doctors = self.service.get_all_doctors()
        if not doctors:
            print("Нет доступных врачей!")
            return
        print("\nДоступные врачи:")
        for i, doctor in enumerate(doctors, 1):
            print(f"{i}. {doctor}")

        doctor_choice = input("Выберите номер врача: ").strip()
        if not doctor_choice.isdigit():
            print("Введите номер!")
            return

        # Выбор кабинета
        rooms = self.service.rooms
        if not rooms:
            print("Нет доступных кабинетов!")
            return
        print("\nДоступные кабинеты:")
        for i, room in enumerate(rooms, 1):
            print(f"{i}. {room}")

        room_choice = input("Выберите номер кабинета: ").strip()
        if not room_choice.isdigit():
            print("Введите номер!")
            return

        # Выбор услуги
        services = self.service.services
        if not services:
            print("Нет доступных услуг!")
            return
        print("\nДоступные услуги:")
        for i, service in enumerate(services, 1):
            print(f"{i}. {service}")

        service_choice = input("Выберите номер услуги: ").strip()
        if not service_choice.isdigit():
            print("Введите номер!")
            return

        # Дополнительная информация
        date = self.get_valid_input("Дата приема (ГГГГ-ММ-ДД): ", self.validator.validate_appointment_date)
        if not date: return

        time = self.get_valid_input("Время приема (ЧЧ:ММ): ", self.validator.validate_appointment_time)
        if not time: return

        reason = self.get_valid_input("Причина визита: ", self.validator.validate_reason)
        if not reason: return

        try:
            patient_choice = int(patient_choice) - 1
            doctor_choice = int(doctor_choice) - 1
            room_choice = int(room_choice) - 1
            service_choice = int(service_choice) - 1

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

        print(f"\nПоликлиника: {self.service.name}")
        print(f"Адрес: {self.service.address}")

        self.view_patients()
        self.view_doctors()
        self.view_departments()
        self.view_rooms()
        self.view_services()
        self.view_appointments()

    def run(self):
        """Запускает главный цикл приложения."""
        print("🚀 Запуск системы управления поликлиникой")

        while True:
            self.display_main_menu()
            choice = input("Выберите действие: ").strip()

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
                print("До свидания!")
                break
            else:
                print("Неверный выбор! Попробуйте снова.")


def main():
    """Основная функция для демонстрации работы системы."""
    app = PolyclinicApp()
    app.run()


if __name__ == "__main__":
    main()