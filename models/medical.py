from typing import List, Dict, Any
from .person import Patient, Doctor

class MedicalService:
    """Класс медицинской услуги."""

    def __init__(self, service_id: int, name: str, description: str,
                 cost: float, duration: int) -> None:
        self.service_id = service_id
        self.name = name
        self.description = description
        self.cost = cost
        self.duration = duration

    def __str__(self) -> str:
        return f"{self.name} ({self.cost} руб.)"

class Diagnosis:
    """Класс медицинского диагноза."""

    def __init__(self, diagnosis_id: int, code: str, name: str,
                 description: str) -> None:
        self.diagnosis_id = diagnosis_id
        self.code = code
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f"{self.code}: {self.name}"

class Prescription:
    """Класс медицинского назначения."""

    def __init__(self, prescription_id: int, medication: str,
                 dosage: str, frequency: str, duration: str) -> None:
        self.prescription_id = prescription_id
        self.medication = medication
        self.dosage = dosage
        self.frequency = frequency
        self.duration = duration

    def __str__(self) -> str:
        return f"{self.medication} - {self.dosage}"

class MedicalRecord:
    """Класс медицинской карты пациента."""

    def __init__(self, record_id: int, patient: Patient) -> None:
        self.record_id = record_id
        self.patient = patient
        self.entries: List[Dict[str, Any]] = []
        patient.medical_record = self

    def add_entry(self, entry_date: str, doctor: Doctor, diagnosis: Diagnosis,
                 symptoms: str, treatment: str,
                 prescriptions: List[Prescription]) -> None:
        """Добавляет запись в медицинскую карту."""
        entry = {
            "entry_id": len(self.entries) + 1,
            "entry_date": entry_date,
            "doctor": doctor,
            "diagnosis": diagnosis,
            "symptoms": symptoms,
            "treatment": treatment,
            "prescriptions": prescriptions
        }
        self.entries.append(entry)

    def __str__(self) -> str:
        return f"Мед. карта #{self.record_id}"