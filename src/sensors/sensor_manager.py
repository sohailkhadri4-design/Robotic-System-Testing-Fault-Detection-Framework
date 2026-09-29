from dataclasses import dataclass
from typing import Optional


@dataclass
class SensorReading:
    name: str
    value: Optional[float]
    timestamp: float
    available: bool = True


class SimulatedSensor:
    """Hardware-independent sensor used for repeatable tests."""

    def __init__(self, name: str, value: Optional[float] = 25.0, available: bool = True):
        self.name = name
        self.value = value
        self.available = available

    def read(self, timestamp: float) -> SensorReading:
        return SensorReading(self.name, self.value, timestamp, self.available)


class SensorManager:
    def __init__(self):
        self._sensors = {}

    def register(self, sensor: SimulatedSensor) -> None:
        self._sensors[sensor.name] = sensor

    def read(self, name: str, timestamp: float) -> SensorReading:
        sensor = self._sensors.get(name)
        if sensor is None:
            return SensorReading(name, None, timestamp, False)
        return sensor.read(timestamp)
