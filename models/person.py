from typing import Optional

class Person:
    """Базовый класс для всех персон в системе."""
    @property
    def patient_id(self):
        return self.person_id

    def __init__(self, person_id: int, first_name: str, last_name: str,
                 birth_date: str, phone: str) -> None:
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.phone = phone

    def get_full_name(self) -> str:
        """Возвращает полное имя персоны."""
        return f"{self.last_name} {self.first_name}"

    def __str__(self) -> str:
        return f"{self.get_full_name()} (ID: {self.person_id})"

class Patient(Person):
    """Класс пациента поликлиники."""

    def __init__(self, patient_id: int, first_name: str, last_name: str,
                 birth_date: str, phone: str, insurance_number: str) -> None:
        super().__init__(patient_id, first_name, last_name, birth_date, phone)
        self.insurance_number = insurance_number
        self.medical_record: Optional['MedicalRecord'] = None

    def __str__(self) -> str:
        return f"Пациент {self.get_full_name()}"

class Doctor(Person):
    """Класс врача поликлиники."""
    @property
    def doctor_id(self):
        return self.person_id

    def __init__(self, doctor_id: int, first_name: str, last_name: str,
                 birth_date: str, phone: str, specialization: str,
                 license_number: str) -> None:
        super().__init__(doctor_id, first_name, last_name, birth_date, phone)
        self.specialization = specialization
        self.license_number = license_number

    def __str__(self) -> str:
        return f"Доктор {self.get_full_name()} ({self.specialization})"