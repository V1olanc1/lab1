import json
import xml.etree.ElementTree as ET
from .polyclinic_service import PolyclinicService


class PolyclinicFileManager:
    """Менеджер для сохранения и загрузки данных поликлиники."""

    @staticmethod
    def save_to_json(service: PolyclinicService, filename: str) -> None:
        """Сохраняет данные поликлиники в JSON файл."""
        try:
            data = {
                "name": service.name,
                "address": service.address,
                "patients": [
                    {
                        "patient_id": p.patient_id,
                        "first_name": p.first_name,
                        "last_name": p.last_name,
                        "birth_date": p.birth_date,
                        "phone": p.phone,
                        "insurance_number": p.insurance_number
                    } for p in service.patients
                ],
                "doctors": [
                    {
                        "doctor_id": d.doctor_id,
                        "first_name": d.first_name,
                        "last_name": d.last_name,
                        "birth_date": d.birth_date,
                        "phone": d.phone,
                        "specialization": d.specialization,
                        "license_number": d.license_number
                    } for d in service.doctors
                ],
                "departments": [
                    {
                        "department_id": d.department_id,
                        "name": d.name,
                        "floor": d.floor,
                        "head_doctor_id": d.head_doctor.doctor_id
                    } for d in service.departments
                ],
                "rooms": [
                    {
                        "room_id": r.room_id,
                        "room_number": r.room_number,
                        "floor": r.floor,
                        "room_type": r.room_type,
                        "department_id": r.department.department_id
                    } for r in service.rooms
                ],
                "services": [
                    {
                        "service_id": s.service_id,
                        "name": s.name,
                        "description": s.description,
                        "cost": s.cost,
                        "duration": s.duration
                    } for s in service.services
                ]
            }

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Данные успешно сохранены в {filename}")

        except Exception as e:
            print(f"Ошибка при сохранении в JSON: {e}")

    @staticmethod
    def load_from_json(filename: str) -> PolyclinicService:
        """Загружает данные поликлиники из JSON файла."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            service = PolyclinicService(data["name"], data["address"])

            # Загрузка пациентов
            for patient_data in data["patients"]:
                service.create_patient(
                    patient_data["first_name"],
                    patient_data["last_name"],
                    patient_data["birth_date"],
                    patient_data["phone"],
                    patient_data["insurance_number"]
                )

            # Загрузка врачей
            for doctor_data in data["doctors"]:
                service.create_doctor(
                    doctor_data["first_name"],
                    doctor_data["last_name"],
                    doctor_data["birth_date"],
                    doctor_data["phone"],
                    doctor_data["specialization"],
                    doctor_data["license_number"]
                )

            # Загрузка отделений
            if "departments" in data:
                for department_data in data["departments"]:
                    service.create_department(
                        department_data["name"],
                        department_data["floor"],
                        department_data["head_doctor_id"]
                    )

            # Загрузка кабинетов
            if "rooms" in data:
                for room_data in data["rooms"]:
                    service.create_room(
                        room_data["room_number"],
                        room_data["floor"],
                        room_data["room_type"],
                        room_data["department_id"]
                    )

            # Загрузка услуг
            if "services" in data:
                for service_data in data["services"]:
                    service.create_service(
                        service_data["name"],
                        service_data["description"],
                        service_data["cost"],
                        service_data["duration"]
                    )

            print(f"Данные успешно загружены из {filename}")
            print(f"Данные успешно загружены из {filename}")
            print(f"Загружено: {len(service.patients)} пациентов, "
                  f"{len(service.doctors)} врачей, "
                  f"{len(service.departments)} отделений, "
                  f"{len(service.rooms)} кабинетов, "
                  f"{len(service.services)} услуг")
            return service

        except Exception as e:
            print(f"Ошибка при загрузке из JSON: {e}")
            return PolyclinicService("Восстановленная поликлиника", "Неизвестный адрес")

    @staticmethod
    def save_to_xml(service: PolyclinicService, filename: str) -> None:
        """Сохраняет данные поликлиники в XML файл."""
        try:
            root = ET.Element("polyclinic")

            ET.SubElement(root, "name").text = service.name
            ET.SubElement(root, "address").text = service.address

            patients_elem = ET.SubElement(root, "patients")
            for patient in service.patients:
                patient_elem = ET.SubElement(patients_elem, "patient")
                ET.SubElement(patient_elem, "id").text = str(patient.patient_id)
                ET.SubElement(patient_elem, "first_name").text = patient.first_name
                ET.SubElement(patient_elem, "last_name").text = patient.last_name
                ET.SubElement(patient_elem, "birth_date").text = patient.birth_date
                ET.SubElement(patient_elem, "phone").text = patient.phone
                ET.SubElement(patient_elem, "insurance_number").text = patient.insurance_number

            doctors_elem = ET.SubElement(root, "doctors")
            for doctor in service.doctors:
                doctor_elem = ET.SubElement(doctors_elem, "doctor")
                ET.SubElement(doctor_elem, "id").text = str(doctor.doctor_id)
                ET.SubElement(doctor_elem, "first_name").text = doctor.first_name
                ET.SubElement(doctor_elem, "last_name").text = doctor.last_name
                ET.SubElement(doctor_elem, "birth_date").text = doctor.birth_date
                ET.SubElement(doctor_elem, "phone").text = doctor.phone
                ET.SubElement(doctor_elem, "specialization").text = doctor.specialization
                ET.SubElement(doctor_elem, "license_number").text = doctor.license_number

            # Сохранение отделений
            departments_elem = ET.SubElement(root, "departments")
            for department in service.departments:
                department_elem = ET.SubElement(departments_elem, "department")
                ET.SubElement(department_elem, "id").text = str(department.department_id)
                ET.SubElement(department_elem, "name").text = department.name
                ET.SubElement(department_elem, "floor").text = str(department.floor)
                ET.SubElement(department_elem, "head_doctor_id").text = str(department.head_doctor.doctor_id)

            # Сохранение кабинетов
            rooms_elem = ET.SubElement(root, "rooms")
            for room in service.rooms:
                room_elem = ET.SubElement(rooms_elem, "room")
                ET.SubElement(room_elem, "id").text = str(room.room_id)
                ET.SubElement(room_elem, "room_number").text = room.room_number
                ET.SubElement(room_elem, "floor").text = str(room.floor)
                ET.SubElement(room_elem, "room_type").text = room.room_type
                ET.SubElement(room_elem, "department_id").text = str(room.department.department_id)

            # Сохранение услуг
            services_elem = ET.SubElement(root, "services")
            for service_obj in service.services:
                service_elem = ET.SubElement(services_elem, "service")
                ET.SubElement(service_elem, "id").text = str(service_obj.service_id)
                ET.SubElement(service_elem, "name").text = service_obj.name
                ET.SubElement(service_elem, "description").text = service_obj.description
                ET.SubElement(service_elem, "cost").text = str(service_obj.cost)
                ET.SubElement(service_elem, "duration").text = str(service_obj.duration)

            tree = ET.ElementTree(root)
            tree.write(filename, encoding='utf-8', xml_declaration=True)
            print(f"Данные успешно сохранены в {filename}")

        except Exception as e:
            print(f"Ошибка при сохранении в XML: {e}")

    @staticmethod
    def load_from_xml(filename: str) -> PolyclinicService:
        """Загружает данные поликлиники из XML файла."""
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            name = root.find("name").text
            address = root.find("address").text
            service = PolyclinicService(name, address)

            # Загрузка пациентов
            patients_elem = root.find("patients")
            if patients_elem is not None:
                for patient_elem in patients_elem.findall("patient"):
                    try:
                        first_name = patient_elem.find("first_name").text
                        last_name = patient_elem.find("last_name").text
                        birth_date = patient_elem.find("birth_date").text
                        phone = patient_elem.find("phone").text
                        insurance_number = patient_elem.find("insurance_number").text

                        # Создаем пациента через сервис для валидации
                        patient = service.create_patient(
                            first_name, last_name, birth_date, phone, insurance_number
                        )
                    except Exception as e:
                        print(f"Ошибка при загрузке пациента: {e}")
                        continue

            # Загрузка врачей
            doctors_elem = root.find("doctors")
            if doctors_elem is not None:
                for doctor_elem in doctors_elem.findall("doctor"):
                    try:
                        # Получаем все элементы
                        first_name_elem = doctor_elem.find("first_name")
                        last_name_elem = doctor_elem.find("last_name")
                        birth_date_elem = doctor_elem.find("birth_date")
                        phone_elem = doctor_elem.find("phone")
                        specialization_elem = doctor_elem.find("specialization")
                        license_number_elem = doctor_elem.find("license_number")

                        # Проверяем, что все необходимые поля существуют и не None
                        if (first_name_elem is not None and last_name_elem is not None and
                            birth_date_elem is not None and phone_elem is not None and
                            specialization_elem is not None and license_number_elem is not None):

                            first_name = first_name_elem.text
                            last_name = last_name_elem.text
                            birth_date = birth_date_elem.text
                            phone = phone_elem.text
                            specialization = specialization_elem.text
                            license_number = license_number_elem.text

                            # Проверяем, что текстовые значения не None
                            if all([first_name, last_name, birth_date, phone, specialization, license_number]):
                                # Создаем врача через сервис для валидации
                                doctor = service.create_doctor(
                                    first_name, last_name, birth_date, phone,
                                    specialization, license_number
                                )
                            else:
                                print("Не все поля врача содержат текст")
                                continue
                        else:
                            print("Не все поля врача найдены в XML")
                            continue
                    except Exception as e:
                        print(f"Ошибка при загрузке врача: {e}")
                        continue

            # Загрузка отделений
            departments_elem = root.find("departments")
            if departments_elem is not None:
                for department_elem in departments_elem.findall("department"):
                    try:
                        name = department_elem.find("name").text
                        floor = int(department_elem.find("floor").text)
                        head_doctor_id = int(department_elem.find("head_doctor_id").text)

                        # Создаем отделение
                        department = service.create_department(name, floor, head_doctor_id)
                        if not department:
                            print(f"Не удалось создать отделение {name}")
                    except Exception as e:
                        print(f"Ошибка при загрузке отделения: {e}")
                        continue

            # Загрузка кабинетов
            rooms_elem = root.find("rooms")
            if rooms_elem is not None:
                for room_elem in rooms_elem.findall("room"):
                    try:
                        room_number = room_elem.find("room_number").text
                        floor = int(room_elem.find("floor").text)
                        room_type = room_elem.find("room_type").text
                        department_id = int(room_elem.find("department_id").text)

                        # Создаем кабинет
                        room = service.create_room(room_number, floor, room_type, department_id)
                        if not room:
                            print(f"Не удалось создать кабинет {room_number}")
                    except Exception as e:
                        print(f"Ошибка при загрузке кабинета: {e}")
                        continue

            # Загрузка услуг
            services_elem = root.find("services")
            if services_elem is not None:
                for service_elem in services_elem.findall("service"):
                    try:
                        name = service_elem.find("name").text
                        description = service_elem.find("description").text
                        cost = float(service_elem.find("cost").text)
                        duration = int(service_elem.find("duration").text)

                        # Создаем услугу
                        medical_service = service.create_service(name, description, cost, duration)
                    except Exception as e:
                        print(f"Ошибка при загрузке услуги: {e}")
                        continue

            print(f"Данные успешно загружены из {filename}")
            print(f"Загружено: {len(service.patients)} пациентов, "
                  f"{len(service.doctors)} врачей, "
                  f"{len(service.departments)} отделений, "
                  f"{len(service.rooms)} кабинетов, "
                  f"{len(service.services)} услуг")

            return service

        except ET.ParseError as e:
            print(f"Ошибка парсинга XML файла: {e}")
            return PolyclinicService("Восстановленная поликлиника", "Неизвестный адрес")
        except Exception as e:
            print(f"Ошибка при загрузке из XML: {e}")
            return PolyclinicService("Восстановленная поликлиника", "Неизвестный адрес")