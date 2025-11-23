from typing import List, Optional
from models import (
    Patient, Doctor, Department, Room, MedicalService,
    Diagnosis, Appointment, MedicalRecord, NotFoundError, ValidationError, Prescription
)

class PolyclinicService:
    """Сервис для управления данными поликлиники."""

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address

        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []
        self.departments: List[Department] = []
        self.rooms: List[Room] = []
        self.services: List[MedicalService] = []
        self.diagnoses: List[Diagnosis] = []
        self.appointments: List[Appointment] = []
        self.medical_records: List[MedicalRecord] = []

        self._next_patient_id = 1
        self._next_doctor_id = 1
        self._next_department_id = 1
        self._next_room_id = 1
        self._next_service_id = 1
        self._next_diagnosis_id = 1
        self._next_appointment_id = 1
        self._next_record_id = 1
        self._next_prescription_id = 1

    def create_patient(self, first_name: str, last_name: str, birth_date: str,
                      phone: str, insurance_number: str) -> Patient:
        """Создает нового пациента."""
        patient = Patient(self._next_patient_id, first_name, last_name,
                         birth_date, phone, insurance_number)
        self.patients.append(patient)
        self._next_patient_id += 1

        record = MedicalRecord(self._next_record_id, patient)
        self.medical_records.append(record)
        self._next_record_id += 1

        return patient

    def get_patient(self, patient_id: int) -> Optional[Patient]:
        """Возвращает пациента по ID."""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def create_doctor(self, first_name: str, last_name: str, birth_date: str,
                     phone: str, specialization: str,
                     license_number: str) -> Doctor:
        """Создает нового врача."""
        doctor = Doctor(self._next_doctor_id, first_name, last_name,
                       birth_date, phone, specialization, license_number)
        self.doctors.append(doctor)
        self._next_doctor_id += 1
        return doctor

    def get_doctor(self, doctor_id: int) -> Optional[Doctor]:
        """Возвращает врача по ID."""
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def create_department(self, name: str, floor: int,
                         head_doctor_id: int) -> Optional[Department]:
        """Создает новое отделение."""
        head_doctor = self.get_doctor(head_doctor_id)
        if not head_doctor:
            return None

        department = Department(self._next_department_id, name, floor, head_doctor)
        self.departments.append(department)
        self._next_department_id += 1
        return department

    def get_department(self, department_id: int) -> Optional[Department]:
        """Возвращает отделение по ID."""
        for department in self.departments:
            if department.department_id == department_id:
                return department
        return None

    def create_room(self, room_number: str, floor: int, room_type: str,
                   department_id: int) -> Optional[Room]:
        """Создает новый кабинет."""
        department = self.get_department(department_id)
        if not department:
            return None

        room = Room(self._next_room_id, room_number, floor, room_type, department)
        self.rooms.append(room)
        self._next_room_id += 1
        return room

    def get_room(self, room_id: int) -> Optional[Room]:
        """Возвращает кабинет по ID."""
        for room in self.rooms:
            if room.room_id == room_id:
                return room
        return None

    def create_service(self, name: str, description: str,
                      cost: float, duration: int) -> MedicalService:
        """Создает новую медицинскую услугу."""
        service = MedicalService(self._next_service_id, name, description,
                                cost, duration)
        self.services.append(service)
        self._next_service_id += 1
        return service

    def get_service(self, service_id: int) -> Optional[MedicalService]:
        """Возвращает услугу по ID."""
        for service in self.services:
            if service.service_id == service_id:
                return service
        return None

    def create_appointment(self, patient_id: int, doctor_id: int, room_id: int,
                          date: str, time: str, service_id: int,
                          reason: str = "") -> Optional[Appointment]:
        """Создает новую запись на прием."""
        patient = self.get_patient(patient_id)
        doctor = self.get_doctor(doctor_id)
        room = self.get_room(room_id)
        service = self.get_service(service_id)

        if not all([patient, doctor, room, service]):
            raise NotFoundError("Не найдены пациент, врач, кабинет или услуга")

        if self._is_time_slot_taken(doctor, date, time):
            raise ValidationError("Время уже занято")

        appointment = Appointment(self._next_appointment_id, patient, doctor,
                                room, date, time, service, reason)
        self.appointments.append(appointment)
        self._next_appointment_id += 1
        return appointment

    def _is_time_slot_taken(self, doctor: Doctor, date: str, time: str) -> bool:
        """Проверяет, занято ли время у врача."""
        for appointment in self.appointments:
            if (appointment.doctor == doctor and
                appointment.appointment_date == date and
                appointment.appointment_time == time and
                appointment.status != "отменен"):
                return True
        return False

    def get_all_patients(self) -> List[Patient]:
        """Возвращает всех пациентов."""
        return self.patients.copy()

    def get_all_doctors(self) -> List[Doctor]:
        """Возвращает всех врачей."""
        return self.doctors.copy()

    def get_all_appointments(self) -> List[Appointment]:
        """Возвращает все записи."""
        return self.appointments.copy()

    def delete_patient(self, patient_id: int) -> bool:
        """Удаляет пациента по ID."""
        for i, patient in enumerate(self.patients):
            if patient.patient_id == patient_id:
                # Удаляем связанную медицинскую карту
                self.medical_records = [record for record in self.medical_records
                                        if record.patient.patient_id != patient_id]
                # Удаляем связанные записи на прием
                self.appointments = [app for app in self.appointments
                                     if app.patient.patient_id != patient_id]
                # Удаляем пациента
                self.patients.pop(i)
                return True
        return False

    def delete_doctor(self, doctor_id: int) -> bool:
        """Удаляет врача по ID."""
        for i, doctor in enumerate(self.doctors):
            if doctor.doctor_id == doctor_id:
                # Проверяем, используется ли врач как заведующий отделением
                for department in self.departments:
                    if department.head_doctor.doctor_id == doctor_id:
                        return False  # Нельзя удалить врача, который заведует отделением

                # Удаляем связанные записи на прием
                self.appointments = [app for app in self.appointments
                                     if app.doctor.doctor_id != doctor_id]
                # Удаляем врача
                self.doctors.pop(i)
                return True
        return False

    def delete_department(self, department_id: int) -> bool:
        """Удаляет отделение по ID."""
        for i, department in enumerate(self.departments):
            if department.department_id == department_id:
                # Проверяем, есть ли связанные кабинеты
                if any(room.department.department_id == department_id for room in self.rooms):
                    return False  # Нельзя удалить отделение с кабинетами

                # Удаляем отделение
                self.departments.pop(i)
                return True
        return False

    def delete_room(self, room_id: int) -> bool:
        """Удаляет кабинет по ID."""
        for i, room in enumerate(self.rooms):
            if room.room_id == room_id:
                # Проверяем, есть ли связанные записи на прием
                if any(app.room.room_id == room_id for app in self.appointments):
                    return False  # Нельзя удалить кабинет с записями

                # Удаляем кабинет
                self.rooms.pop(i)
                return True
        return False

    def delete_service(self, service_id: int) -> bool:
        """Удаляет услугу по ID."""
        for i, service in enumerate(self.services):
            if service.service_id == service_id:
                # Проверяем, используется ли услуга в записях на прием
                if any(app.service.service_id == service_id for app in self.appointments):
                    return False  # Нельзя удалить услугу, используемую в записях

                # Удаляем услугу
                self.services.pop(i)
                return True
        return False

    def delete_appointment(self, appointment_id: int) -> bool:
        """Удаляет запись на прием по ID."""
        for i, appointment in enumerate(self.appointments):
            if appointment.appointment_id == appointment_id:
                self.appointments.pop(i)
                return True
        return False

    def create_diagnosis(self, code: str, name: str, description: str) -> Diagnosis:
        """Создает новый диагноз."""
        diagnosis = Diagnosis(self._next_diagnosis_id, code, name, description)
        self.diagnoses.append(diagnosis)
        self._next_diagnosis_id += 1
        return diagnosis

    def create_prescription(self, medication: str, dosage: str, frequency: str, duration: str) -> Prescription:
        """Создает новое назначение."""
        prescription = Prescription(self._next_prescription_id, medication, dosage, frequency, duration)
        self._next_prescription_id += 1
        return prescription