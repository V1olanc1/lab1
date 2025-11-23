from services.polyclinic_service import PolyclinicService
from services.file_manager import PolyclinicFileManager


def main():
    """Основная функция для демонстрации работы системы."""
    # Создание сервиса поликлиники
    service = PolyclinicService("Городская поликлиника №1", "ул. Ленина, 10")

    # Добавление тестовых данных
    patient1 = service.create_patient(
        "Иван", "Иванов", "1990-01-01", "+79161112233", "INS001"
    )

    patient2 = service.create_patient(
        "Мария", "Петрова", "1985-05-15", "+79162223344", "INS002"
    )

    doctor1 = service.create_doctor(
        "Алексей", "Смирнов", "1975-03-15", "+79163334455",
        "Терапевт", "MED123456"
    )

    doctor2 = service.create_doctor(
        "Елена", "Козлова", "1980-07-22", "+79164445566",
        "Хирург", "MED654321"
    )

    # Создание отделения и кабинета
    department = service.create_department("Терапевтическое", 1, doctor1.doctor_id)
    room = service.create_room("101", 1, "examination", department.department_id)

    # Создание услуги
    medical_service = service.create_service(
        "Консультация терапевта", "Первичный осмотр терапевта", 1500.0, 30
    )

    # Демонстрация работы
    print("Созданные пациенты:")
    for patient in service.get_all_patients():
        print(f"  - {patient}")

    print("\nСозданные врачи:")
    for doctor in service.get_all_doctors():
        print(f"  - {doctor}")

    print(f"\nСозданное отделение: {department}")
    print(f"Созданный кабинет: {room}")
    print(f"Созданная услуга: {medical_service}")

    # Создание записи на прием
    try:
        appointment = service.create_appointment(
            patient1.patient_id, doctor1.doctor_id, room.room_id,
            "2024-01-15", "10:00", medical_service.service_id, "Обследование"
        )
        print(f"\nСозданная запись: {appointment}")
    except Exception as e:
        print(f"\nОшибка при создании записи: {e}")

    # Сохранение данных
    file_manager = PolyclinicFileManager()
    file_manager.save_to_json(service, "polyclinic_data.json")
    file_manager.save_to_xml(service, "polyclinic_data.xml")

    # Демонстрация загрузки
    print("\n--- Загрузка данных ---")
    loaded_service = file_manager.load_from_xml("polyclinic_data.xml")

if __name__ == "__main__":
    main()