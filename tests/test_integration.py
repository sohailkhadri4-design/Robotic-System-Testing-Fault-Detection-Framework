import time
from src.faults.fault_detector import FaultDetector
from src.motors.motor_controller import SimulatedMotorController
from src.sensors.sensor_manager import SensorManager, SimulatedSensor
from src.sensors.sensor_validator import SensorValidator


def test_sensor_and_motor_validation_flow():
    sensors = SensorManager()
    sensors.register(SimulatedSensor("temperature", 45.0))
    reading = sensors.read("temperature", time.time())
    result = SensorValidator(-20.0, 100.0).validate(reading)
    assert result.valid

    command = SimulatedMotorController().command(60.0, "forward")
    assert command.speed_percent == 60.0

    assert FaultDetector().sensor_fault("temperature", result.reason) is None
