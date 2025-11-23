from typing import List
from .person import Doctor

class Department:
    """Класс отделения поликлиники."""

    def __init__(self, department_id: int, name: str, floor: int,
                 head_doctor: Doctor) -> None:
        self.department_id = department_id
        self.name = name
        self.floor = floor
        self.head_doctor = head_doctor
        self.doctors: List[Doctor] = []

    def add_doctor(self, doctor: Doctor) -> None:
        """Добавляет врача в отделение."""
        self.doctors.append(doctor)

    def __str__(self) -> str:
        return f"Отделение {self.name} (этаж {self.floor})"

class Room:
    """Класс кабинета поликлиника."""

    def __init__(self, room_id: int, room_number: str, floor: int,
                 room_type: str, department: Department) -> None:
        self.room_id = room_id
        self.room_number = room_number
        self.floor = floor
        self.room_type = room_type
        self.department = department

    def __str__(self) -> str:
        return f"Кабинет {self.room_number} ({self.room_type})"