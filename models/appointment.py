from .person import Patient, Doctor
from .structure import Room
from .medical import MedicalService


class Appointment:
    """Класс записи на прием."""

    def __init__(
        self,
        appointment_id: int,
        patient: Patient,
        doctor: Doctor,
        room: Room,
        appointment_date: str,
        appointment_time: str,
        service: MedicalService,
        reason: str = "",
    ) -> None:
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.room = room
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.service = service
        self.reason = reason
        self.status: str = "запланирован"

    def complete(self) -> None:
        """Отмечает прием как завершенный."""
        self.status = "завершен"

    def cancel(self) -> None:
        """Отменяет прием."""
        self.status = "отмене"

    def __str__(self) -> str:
        return (
            f"Прием #{self.appointment_id}: {self.patient.get_full_name()} "
            f"-> {self.doctor.get_full_name()} ({self.appointment_date} "
            f"{self.appointment_time}) - {status_text[self.status]}"
        )
