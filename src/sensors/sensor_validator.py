from dataclasses import dataclass
from .sensor_manager import SensorReading


@dataclass(frozen=True)
class SensorValidation:
    valid: bool
    reason: str


class SensorValidator:
    def __init__(self, minimum: float, maximum: float):
        if minimum >= maximum:
            raise ValueError("minimum must be less than maximum")
        self.minimum = minimum
        self.maximum = maximum

    def validate(self, reading: SensorReading) -> SensorValidation:
        if not reading.available:
            return SensorValidation(False, "SENSOR_UNAVAILABLE")
        if reading.value is None:
            return SensorValidation(False, "INVALID_SENSOR_READING")
        if not self.minimum <= reading.value <= self.maximum:
            return SensorValidation(False, "INVALID_SENSOR_READING")
        return SensorValidation(True, "OK")
