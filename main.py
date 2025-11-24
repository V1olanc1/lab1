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
        if not re.match(r"^[a-zA-Zа-яА-ЯёЁ\s\-]+$", name):
            print(f"{field_name} может содержать только буквы, пробелы и дефисы")
            return False
        return True

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Проверяет номер телефона."""
        cleaned_phone = re.sub(r"[^\d+]", "", phone)

        if (
            (cleaned_phone.startswith("+7") and len(cleaned_phone) == 12)
            or (cleaned_phone.startswith("8") and len(cleaned_phone) == 11)
            or (cleaned_phone.startswith("7") and len(cleaned_phone) == 11)
        ):
            return True

        print(
            "Неверный формат телефона. Используйте: +7XXX..., 8XXX... или 7XXX... (10 цифр после кода)"
        )
        return False

    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Проверяет дату в формате ГГГГ-ММ-ДД."""
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            if date > datetime.now():
                print("Дата не может быть в будущем")
                return False
            return True
        except ValueError:
            print("Неверный формат даты. Используйте: ГГГГ-ММ-ДД")
            return False

    @staticmethod
    def validate_insurance_number(number: str) -> bool:
        """Проверяет номер страховки - только 16 цифр."""
        cleaned_number = re.sub(r"[\s\-]", "", number)

        if not cleaned_number:
            print("Номер страховки не может быть пустым")
            return False

        if len(cleaned_number) != 16:
            print("Номер страховки должен содержать ровно 16 цифр")
            return False

        if not cleaned_number.isdigit():
            print("Номер страховки должен содержать только цифры")
            return False

        return True

    @staticmethod
    def validate_license_number(number: str) -> bool:
        """Проверяет номер лицензии врача."""
        if not number or len(number.strip()) < 5:
            print("Номер лицензии должен содержать минимум 5 символов")
            return False
        if not re.match(r"^[a-zA-Zа-яА-ЯёЁ0-9\-]+$", number):
            print("Номер лицензии может содержать только буквы, цифры и дефисы")
            return False
        return True

    @staticmethod
    def validate_specialization(spec: str) -> bool:
        """Проверяет специализацию врача."""
        if not spec or len(spec.strip()) < 3:
            print("Специализация должна содержать минимум 3 символа")
            return False
        if not re.match(r"^[a-zA-Zа-яА-ЯёЁ\s\-]+$", spec):
            print("Специализация может содержать только буквы, пробелы и дефисы")
            return False
        return True

    @staticmethod
    def validate_floor(floor: str) -> bool:
        """Проверяет номер этажа."""
        try:
            floor_num = int(floor)
            if 1 <= floor_num <= 50:
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
        if not re.match(r"^[a-zA-Zа-яА-ЯёЁ0-9\-\s]+$", number):
            print(
                "Номер кабинета может содержать только буквы, цифры, пробелы и дефисы"
            )
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
            if 1 <= duration_num <= 480:
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
            date = datetime.strptime(date_str, "%Y-%m-%d")
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
            time = datetime.strptime(time_str, "%H:%M")
            hour = time.hour
            if 8 <= hour <= 20:
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

    @staticmethod
    def validate_diagnosis_code(code: str) -> bool:
        """Проверяет код диагноза."""
        if not code or len(code.strip()) < 2:
            print("Код диагноза должен содержать минимум 2 символа")
            return False
        return True

    @staticmethod
    def validate_medication(medication: str) -> bool:
        """Проверяет название лекарства."""
        if not medication or len(medication.strip()) < 2:
            print("Название лекарства должно содержать минимум 2 символа")
            return False
        return True

    @staticmethod
    def validate_dosage(dosage: str) -> bool:
        """Проверяет дозировку."""
        if not dosage or len(dosage.strip()) < 1:
            print("Дозировка не может быть пустой")
            return False
        return True

    @staticmethod
    def validate_symptoms(symptoms: str) -> bool:
        """Проверяет симптомы."""
        if not symptoms or len(symptoms.strip()) < 5:
            print("Описание симптомов должно содержать минимум 5 символов")
            return False
        return True

    @staticmethod
    def validate_treatment(treatment: str) -> bool:
        """Проверяет лечение."""
        if not treatment or len(treatment.strip()) < 5:
            print("Описание лечения должно содержать минимум 5 символов")
            return False
        return True


class PolyclinicApp:
    """Класс приложения поликлиники с меню."""

    def __init__(self):
        self.service = None
        self.file_manager = PolyclinicFileManager()
        self.validator = Validator()

    def get_valid_input(
        self, prompt: str, validation_func, field_name: str = "", max_attempts: int = 3
    ):
        """Получает валидный ввод от пользователя."""
        attempts = 0
        while attempts < max_attempts:
            value = input(prompt).strip()
            if (
                validation_func(value, field_name)
                if field_name
                else validation_func(value)
            ):
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
        print("9. Медицинские карты и диагнозы")
        print("10. Просмотр всех данных")
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
        """Меню загрузки данных."""
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
            print("3. Удалить пациента")
            print("4. Назад")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.view_patients()
            elif choice == "3":
                self.delete_patient()
            elif choice == "4":
                break
            else:
                print("Неверный выбор!")

    def add_patient(self):
        """Добавляет нового пациента."""
        print("\n--- ДОБАВЛЕНИЕ ПАЦИЕНТА ---")

        first_name = self.get_valid_input("Имя: ", self.validator.validate_name, "Имя")
        if not first_name:
            return

        last_name = self.get_valid_input(
            "Фамилия: ", self.validator.validate_name, "Фамилия"
        )
        if not last_name:
            return

        birth_date = self.get_valid_input(
            "Дата рождения (ГГГГ-ММ-ДД): ", self.validator.validate_date
        )
        if not birth_date:
            return

        phone = self.get_valid_input("Телефон: ", self.validator.validate_phone)
        if not phone:
            return

        insurance_number = self.get_valid_input(
            "Номер страховки (16 цифр): ", self.validator.validate_insurance_number
        )
        if not insurance_number:
            return

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
            medical_record = next(
                (
                    record
                    for record in self.service.medical_records
                    if record.patient.patient_id == patient.patient_id
                ),
                None,
            )
            record_info = (
                " (есть мед. карта)"
                if medical_record and medical_record.entries
                else " (нет записей)"
            )
            print(
                f"{i}. {patient} (Тел: {patient.phone}, Страховка: {patient.insurance_number}){record_info}"
            )

    def delete_patient(self):
        """Удаляет пациента."""
        patients = self.service.get_all_patients()
        if not patients:
            print("Нет пациентов для удаления")
            return

        print("\n--- УДАЛЕНИЕ ПАЦИЕНТА ---")
        self.view_patients()

        try:
            patient_choice = (
                int(input("Выберите номер пациента для удаления: ").strip()) - 1
            )
            if 0 <= patient_choice < len(patients):
                patient = patients[patient_choice]
                confirm = (
                    input(
                        f"Вы уверены, что хотите удалить пациента {patient}? (да/нет): "
                    )
                    .strip()
                    .lower()
                )
                if confirm == "да":
                    if self.service.delete_patient(patient.patient_id):
                        print(f"Пациент {patient} удален")
                    else:
                        print("Не удалось удалить пациента")
                else:
                    print("Удаление отменено")
            else:
                print("Неверный выбор пациента!")
        except ValueError:
            print("Введите корректный номер!")

    def doctors_menu(self):
        """Меню управления врачами."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- УПРАВЛЕНИЕ ВРАЧАМИ ---")
            print("1. Добавить врача")
            print("2. Просмотреть всех врачей")
            print("3. Удалить врача")
            print("4. Назад")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.add_doctor()
            elif choice == "2":
                self.view_doctors()
            elif choice == "3":
                self.delete_doctor()
            elif choice == "4":
                break
            else:
                print("Неверный выбор!")

    def add_doctor(self):
        """Добавляет нового врача."""
        print("\n--- ДОБАВЛЕНИЕ ВРАЧА ---")

        first_name = self.get_valid_input("Имя: ", self.validator.validate_name, "Имя")
        if not first_name:
            return

        last_name = self.get_valid_input(
            "Фамилия: ", self.validator.validate_name, "Фамилия"
        )
        if not last_name:
            return

        birth_date = self.get_valid_input(
            "Дата рождения (ГГГГ-ММ-ДД): ", self.validator.validate_date
        )
        if not birth_date:
            return

        phone = self.get_valid_input("Телефон: ", self.validator.validate_phone)
        if not phone:
            return

        specialization = self.get_valid_input(
            "Специализация: ", self.validator.validate_specialization
        )
        if not specialization:
            return

        license_number = self.get_valid_input(
            "Номер лицензии: ", self.validator.validate_license_number
        )
        if not license_number:
            return

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
            print(
                f"{i}. {doctor} (Тел: {doctor.phone}, Лицензия: {doctor.license_number})"
            )

    def delete_doctor(self):
        """Удаляет врача."""
        doctors = self.service.get_all_doctors()
        if not doctors:
            print("Нет врачей для удаления")
            return

        print("\n--- УДАЛЕНИЕ ВРАЧА ---")
        self.view_doctors()

        try:
            doctor_choice = (
                int(input("Выберите номер врача для удаления: ").strip()) - 1
            )
            if 0 <= doctor_choice < len(doctors):
                doctor = doctors[doctor_choice]
                confirm = (
                    input(f"Вы уверены, что хотите удалить врача {doctor}? (да/нет): ")
                    .strip()
                    .lower()
                )
                if confirm == "да":
                    if self.service.delete_doctor(doctor.doctor_id):
                        print(f"Врач {doctor} удален")
                    else:
                        print(
                            "Не удалось удалить врача (возможно, он заведует отделением)"
                        )
                else:
                    print("Удаление отменено")
            else:
                print("Неверный выбор врача!")
        except ValueError:
            print("Введите корректный номер!")

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
            print("5. Удалить отделение")
            print("6. Удалить кабинет")
            print("7. Назад")
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
                self.delete_department()
            elif choice == "6":
                self.delete_room()
            elif choice == "7":
                break
            else:
                print("Неверный выбор!")

    def add_department(self):
        """Добавляет новое отделение."""
        print("\n--- ДОБАВЛЕНИЕ ОТДЕЛЕНИЯ ---")

        name = self.get_valid_input(
            "Название отделения: ", self.validator.validate_name, "Название отделения"
        )
        if not name:
            return

        floor = self.get_valid_input("Этаж: ", self.validator.validate_floor)
        if not floor:
            return

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
                department = self.service.create_department(
                    name, int(floor), head_doctor_id
                )
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

        room_number = self.get_valid_input(
            "Номер кабинета: ", self.validator.validate_room_number
        )
        if not room_number:
            return

        floor = self.get_valid_input("Этаж: ", self.validator.validate_floor)
        if not floor:
            return

        room_type = input("Тип кабинета : ")
        if not room_type:
            return

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
                room = self.service.create_room(
                    room_number, int(floor), room_type, department_id
                )
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
            print(
                f"{i}. {department} (Заведующий: {department.head_doctor.get_full_name()})"
            )

    def view_rooms(self):
        """Просматривает все кабинеты."""
        rooms = self.service.rooms
        if not rooms:
            print("Кабинеты не найдены")
            return

        print("\n--- СПИСОК КАБИНЕТОВ ---")
        for i, room in enumerate(rooms, 1):
            print(f"{i}. {room} (Отделение: {room.department.name})")

    def delete_department(self):
        """Удаляет отделение."""
        departments = self.service.departments
        if not departments:
            print("Нет отделений для удаления")
            return

        print("\n--- УДАЛЕНИЕ ОТДЕЛЕНИЯ ---")
        self.view_departments()

        try:
            dept_choice = (
                int(input("Выберите номер отделения для удаления: ").strip()) - 1
            )
            if 0 <= dept_choice < len(departments):
                department = departments[dept_choice]
                confirm = (
                    input(
                        f"Вы уверены, что хотите удалить отделение {department}? (да/нет): "
                    )
                    .strip()
                    .lower()
                )
                if confirm == "да":
                    if self.service.delete_department(department.department_id):
                        print(f"Отделение {department} удалено")
                    else:
                        print(
                            "Не удалось удалить отделение (возможно, в нем есть кабинеты)"
                        )
                else:
                    print("Удаление отменено")
            else:
                print("Неверный выбор отделения!")
        except ValueError:
            print("Введите корректный номер!")

    def delete_room(self):
        """Удаляет кабинет."""
        rooms = self.service.rooms
        if not rooms:
            print("Нет кабинетов для удаления")
            return

        print("\n--- УДАЛЕНИЕ КАБИНЕТА ---")
        self.view_rooms()

        try:
            room_choice = (
                int(input("Выберите номер кабинета для удаления: ").strip()) - 1
            )
            if 0 <= room_choice < len(rooms):
                room = rooms[room_choice]
                confirm = (
                    input(f"Вы уверены, что хотите удалить кабинет {room}? (да/нет): ")
                    .strip()
                    .lower()
                )
                if confirm == "да":
                    if self.service.delete_room(room.room_id):
                        print(f"Кабинет {room} удален")
                    else:
                        print(
                            "Не удалось удалить кабинет (возможно, на него есть записи)"
                        )
                else:
                    print("Удаление отменено")
            else:
                print("Неверный выбор кабинета!")
        except ValueError:
            print("Введите корректный номер!")

    def services_menu(self):
        """Меню управления услугами."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- УПРАВЛЕНИЕ УСЛУГАМИ ---")
            print("1. Добавить услугу")
            print("2. Просмотреть все услуги")
            print("3. Удалить услугу")
            print("4. Назад")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.add_service()
            elif choice == "2":
                self.view_services()
            elif choice == "3":
                self.delete_service()
            elif choice == "4":
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
        if not cost:
            return

        duration = self.get_valid_input(
            "Длительность (мин): ", self.validator.validate_duration
        )
        if not duration:
            return

        try:
            service = self.service.create_service(
                name, description, float(cost), int(duration)
            )
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

    def delete_service(self):
        """Удаляет услугу."""
        services = self.service.services
        if not services:
            print("Нет услуг для удаления")
            return

        print("\n--- УДАЛЕНИЕ УСЛУГИ ---")
        self.view_services()

        try:
            service_choice = (
                int(input("Выберите номер услуги для удаления: ").strip()) - 1
            )
            if 0 <= service_choice < len(services):
                service = services[service_choice]
                confirm = (
                    input(
                        f"Вы уверены, что хотите удалить услугу {service}? (да/нет): "
                    )
                    .strip()
                    .lower()
                )
                if confirm == "да":
                    if self.service.delete_service(service.service_id):
                        print(f"Услуга {service} удалена")
                    else:
                        print(
                            "Не удалось удалить услугу (возможно, она используется в записях)"
                        )
                else:
                    print("Удаление отменено")
            else:
                print("Неверный выбор услуги!")
        except ValueError:
            print("Введите корректный номер!")

    def appointments_menu(self):
        """Меню управления записями на прием."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- ЗАПИСИ НА ПРИЕМ ---")
            print("1. Создать запись")
            print("2. Просмотреть все записи")
            print("3. Удалить запись")
            print("4. Назад")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.create_appointment()
            elif choice == "2":
                self.view_appointments()
            elif choice == "3":
                self.delete_appointment()
            elif choice == "4":
                break
            else:
                print("Неверный выбор!")

    def create_appointment(self):
        """Создает новую запись на прием."""
        print("\n--- СОЗДАНИЕ ЗАПИСИ НА ПРИЕМ ---")

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

        date = self.get_valid_input(
            "Дата приема (ГГГГ-ММ-ДД): ", self.validator.validate_appointment_date
        )
        if not date:
            return

        time = self.get_valid_input(
            "Время приема (ЧЧ:ММ): ", self.validator.validate_appointment_time
        )
        if not time:
            return

        reason = self.get_valid_input(
            "Причина визита: ", self.validator.validate_reason
        )
        if not reason:
            return

        try:
            patient_choice = int(patient_choice) - 1
            doctor_choice = int(doctor_choice) - 1
            room_choice = int(room_choice) - 1
            service_choice = int(service_choice) - 1

            if (
                0 <= patient_choice < len(patients)
                and 0 <= doctor_choice < len(doctors)
                and 0 <= room_choice < len(rooms)
                and 0 <= service_choice < len(services)
            ):

                appointment = self.service.create_appointment(
                    patients[patient_choice].patient_id,
                    doctors[doctor_choice].doctor_id,
                    rooms[room_choice].room_id,
                    date,
                    time,
                    services[service_choice].service_id,
                    reason,
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

    def delete_appointment(self):
        """Удаляет запись на прием."""
        appointments = self.service.get_all_appointments()
        if not appointments:
            print("Нет записей для удаления")
            return

        print("\n--- УДАЛЕНИЕ ЗАПИСИ ---")
        self.view_appointments()

        try:
            appointment_choice = (
                int(input("Выберите номер записи для удаления: ").strip()) - 1
            )
            if 0 <= appointment_choice < len(appointments):
                appointment = appointments[appointment_choice]
                confirm = (
                    input(
                        f"Вы уверены, что хотите удалить запись {appointment}? (да/нет): "
                    )
                    .strip()
                    .lower()
                )
                if confirm == "да":
                    if self.service.delete_appointment(appointment.appointment_id):
                        print(f"Запись {appointment} удалена")
                    else:
                        print("Не удалось удалить запись")
                else:
                    print("Удаление отменено")
            else:
                print("Неверный выбор записи!")
        except ValueError:
            print("Введите корректный номер!")

    def medical_records_menu(self):
        """Меню управления медицинскими картами и диагнозами."""
        if not self.service:
            print("Сначала создайте поликлинику!")
            return

        while True:
            print("\n--- МЕДИЦИНСКИЕ КАРТЫ И ДИАГНОЗЫ ---")
            print("1. Просмотреть все медицинские карты")
            print("2. Добавить диагноз")
            print("3. Просмотреть все диагнозы")
            print("4. Добавить запись в медицинскую карту")
            print("5. Просмотреть медицинскую карту пациента")
            print("6. Назад")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.view_all_medical_records()
            elif choice == "2":
                self.add_diagnosis()
            elif choice == "3":
                self.view_diagnoses()
            elif choice == "4":
                self.add_medical_record_entry()
            elif choice == "5":
                self.view_patient_medical_record()
            elif choice == "6":
                break
            else:
                print("Неверный выбор!")

    def view_all_medical_records(self):
        """Просматривает все медицинские карты."""
        if not self.service.medical_records:
            print("Медицинские карты не найдены")
            return

        print("\n--- ВСЕ МЕДИЦИНСКИЕ КАРТЫ ---")
        for i, record in enumerate(self.service.medical_records, 1):
            entries_count = len(record.entries)
            print(f"{i}. {record} - {entries_count} записей")

    def add_diagnosis(self):
        """Добавляет новый диагноз."""
        print("\n--- ДОБАВЛЕНИЕ ДИАГНОЗА ---")

        code = self.get_valid_input(
            "Код диагноза: ", self.validator.validate_diagnosis_code
        )
        if not code:
            return

        name = input("Название диагноза: ").strip()
        if not name:
            print("Название диагноза не может быть пустым")
            return

        description = input("Описание диагноза: ").strip()
        if not description:
            print("Описание диагноза не может быть пустым")
            return

        try:
            diagnosis = self.service.create_diagnosis(code, name, description)
            print(f"Диагноз добавлен: {diagnosis}")
        except Exception as e:
            print(f"Ошибка при добавлении диагноза: {e}")

    def view_diagnoses(self):
        """Просматривает все диагнозы."""
        diagnoses = self.service.diagnoses
        if not diagnoses:
            print("Диагнозы не найдены")
            return

        print("\n--- СПИСОК ДИАГНОЗОВ ---")
        for i, diagnosis in enumerate(diagnoses, 1):
            print(f"{i}. {diagnosis}")

    def add_medical_record_entry(self):
        """Добавляет запись в медицинскую карту."""
        print("\n--- ДОБАВЛЕНИЕ ЗАПИСИ В МЕДИЦИНСКУЮ КАРТУ ---")

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

        diagnoses = self.service.diagnoses
        if not diagnoses:
            print("Нет доступных диагнозов!")
            return
        print("\nДоступные диагнозы:")
        for i, diagnosis in enumerate(diagnoses, 1):
            print(f"{i}. {diagnosis}")

        diagnosis_choice = input("Выберите номер диагноза: ").strip()
        if not diagnosis_choice.isdigit():
            print("Введите номер!")
            return

        entry_date = self.get_valid_input(
            "Дата осмотра (ГГГГ-ММ-ДД): ", self.validator.validate_date
        )
        if not entry_date:
            return

        symptoms = self.get_valid_input("Симптомы: ", self.validator.validate_symptoms)
        if not symptoms:
            return

        treatment = self.get_valid_input("Лечение: ", self.validator.validate_treatment)
        if not treatment:
            return

        print("\n--- ДОБАВЛЕНИЕ НАЗНАЧЕНИЙ ---")
        prescriptions = []
        while True:
            print("\nДобавить назначение?")
            print("1. Добавить лекарство")
            print("2. Закончить ввод назначений")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                medication = self.get_valid_input(
                    "Название лекарства: ", self.validator.validate_medication
                )
                if not medication:
                    continue

                dosage = self.get_valid_input(
                    "Дозировка: ", self.validator.validate_dosage
                )
                if not dosage:
                    continue

                frequency = input("Частота приема: ").strip()
                if not frequency:
                    print("Частота приема не может быть пустой")
                    continue

                duration = input("Длительность приема: ").strip()
                if not duration:
                    print("Длительность приема не может быть пустой")
                    continue

                try:
                    prescription = self.service.create_prescription(
                        medication, dosage, frequency, duration
                    )
                    prescriptions.append(prescription)
                    print(f"Назначение добавлено: {prescription}")
                except Exception as e:
                    print(f"Ошибка при добавлении назначения: {e}")

            elif choice == "2":
                break
            else:
                print("Неверный выбор!")

        try:
            patient_choice = int(patient_choice) - 1
            doctor_choice = int(doctor_choice) - 1
            diagnosis_choice = int(diagnosis_choice) - 1

            if (
                0 <= patient_choice < len(patients)
                and 0 <= doctor_choice < len(doctors)
                and 0 <= diagnosis_choice < len(diagnoses)
            ):

                patient = patients[patient_choice]
                doctor = doctors[doctor_choice]
                diagnosis = diagnoses[diagnosis_choice]

                medical_record = next(
                    (
                        record
                        for record in self.service.medical_records
                        if record.patient.patient_id == patient.patient_id
                    ),
                    None,
                )

                if medical_record:
                    medical_record.add_entry(
                        entry_date,
                        doctor,
                        diagnosis,
                        symptoms,
                        treatment,
                        prescriptions,
                    )
                    print(f"Запись добавлена в медицинскую карту пациента {patient}")
                else:
                    print("Медицинская карта для пациента не найдена")
            else:
                print("Неверный выбор!")
        except Exception as e:
            print(f"Ошибка при добавлении записи: {e}")

    def view_patient_medical_record(self):
        """Просматривает медицинскую карту пациента."""
        patients = self.service.get_all_patients()
        if not patients:
            print("Нет доступных пациентов!")
            return

        print("\n--- ПРОСМОТР МЕДИЦИНСКОЙ КАРТЫ ---")
        self.view_patients()

        try:
            patient_choice = int(input("Выберите номер пациента: ").strip()) - 1
            if 0 <= patient_choice < len(patients):
                patient = patients[patient_choice]
                medical_record = next(
                    (
                        record
                        for record in self.service.medical_records
                        if record.patient.patient_id == patient.patient_id
                    ),
                    None,
                )

                if medical_record and medical_record.entries:
                    print(f"\n--- МЕДИЦИНСКАЯ КАРТА: {patient} ---")
                    for i, entry in enumerate(medical_record.entries, 1):
                        print(f"\nЗапись #{i}:")
                        print(f"  Дата: {entry['entry_date']}")
                        print(f"  Врач: {entry['doctor'].get_full_name()}")
                        print(f"  Диагноз: {entry['diagnosis']}")
                        print(f"  Симптомы: {entry['symptoms']}")
                        print(f"  Лечение: {entry['treatment']}")
                        if entry["prescriptions"]:
                            print("  Назначения:")
                            for j, prescription in enumerate(entry["prescriptions"], 1):
                                print(f"    {j}. {prescription}")
                else:
                    print(f"Медицинская карта пациента {patient} пуста или не найдена")
            else:
                print("Неверный выбор пациента!")
        except ValueError:
            print("Введите корректный номер!")

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
        self.view_diagnoses()
        self.view_all_medical_records()

    def run(self):
        """Запускает главный цикл приложения."""
        print("Запуск системы управления поликлиникой")

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
                self.medical_records_menu()
            elif choice == "10":
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
