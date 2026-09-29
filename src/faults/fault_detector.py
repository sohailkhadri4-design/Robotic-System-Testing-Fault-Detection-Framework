from dataclasses import dataclass
from .fault_types import FaultType


@dataclass(frozen=True)
class FaultEvent:
    fault_type: FaultType
    source: str
    detail: str


class FaultDetector:
    def sensor_fault(self, source: str, reason: str):
        if reason == "OK":
            return None
        try:
            fault_type = FaultType(reason)
        except ValueError:
            fault_type = FaultType.INVALID_SENSOR_READING
        return FaultEvent(fault_type, source, reason)

    def motor_fault(self, source: str, reason: str) -> FaultEvent:
        try:
            fault_type = FaultType(reason)
        except ValueError:
            fault_type = FaultType.MOTOR_CONTROLLER_FAULT
        return FaultEvent(fault_type, source, reason)
