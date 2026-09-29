from src.faults.fault_detector import FaultDetector
from src.faults.fault_types import FaultType


def test_sensor_fault_detection():
    event = FaultDetector().sensor_fault("temperature", "SENSOR_UNAVAILABLE")
    assert event.fault_type == FaultType.SENSOR_UNAVAILABLE


def test_unknown_sensor_reason_is_invalid():
    event = FaultDetector().sensor_fault("temperature", "UNKNOWN")
    assert event.fault_type == FaultType.INVALID_SENSOR_READING
