import time
from src.faults.fault_detector import FaultDetector
from src.logging.test_logger import StructuredTestLogger
from src.motors.motor_controller import SimulatedMotorController
from src.sensors.sensor_manager import SensorManager, SimulatedSensor
from src.sensors.sensor_validator import SensorValidator


def main():
    logger = StructuredTestLogger()
    sensors = SensorManager()
    sensors.register(SimulatedSensor("temperature", 32.5))
    reading = sensors.read("temperature", time.time())
    result = SensorValidator(-20.0, 100.0).validate(reading)
    logger.event("sensor_validation", sensor=reading.name, value=reading.value,
                 status="PASS" if result.valid else "FAIL", reason=result.reason)

    motor = SimulatedMotorController()
    command = motor.command(40.0, "forward")
    logger.event("motor_command", speed_percent=command.speed_percent,
                 direction=command.direction, status="PASS")

    fault = FaultDetector().sensor_fault("temperature", "SENSOR_UNAVAILABLE")
    if fault:
        logger.event("fault_detected", source=fault.source,
                     fault_type=fault.fault_type.value, detail=fault.detail)


if __name__ == "__main__":
    main()
