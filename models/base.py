class MedicalError(Exception):
    """Базовое исключение для медицинской системы."""

    pass


class NotFoundError(MedicalError):
    """Исключение при ненайденном объекте."""

    pass


class ValidationError(MedicalError):
    """Исключение при невалидных данных."""

    pass
