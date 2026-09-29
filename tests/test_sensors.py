import time
from src.sensors.sensor_manager import SensorManager, SimulatedSensor
from src.sensors.sensor_validator import SensorValidator


def test_valid_sensor_reading():
    manager = SensorManager()
    manager.register(SimulatedSensor("temperature", 30.0))
    result = SensorValidator(-20.0, 100.0).validate(manager.read("temperature", time.time()))
    assert result.valid
    assert result.reason == "OK"


def test_unavailable_sensor():
    manager = SensorManager()
    manager.register(SimulatedSensor("temperature", 30.0, available=False))
    result = SensorValidator(-20.0, 100.0).validate(manager.read("temperature", time.time()))
    assert not result.valid
    assert result.reason == "SENSOR_UNAVAILABLE"


def test_out_of_range_sensor():
    manager = SensorManager()
    manager.register(SimulatedSensor("temperature", 150.0))
    result = SensorValidator(-20.0, 100.0).validate(manager.read("temperature", time.time()))
    assert not result.valid
    assert result.reason == "INVALID_SENSOR_READING"
