import pytest
from src.motors.motor_controller import SimulatedMotorController
from src.motors.motor_validator import MotorValidator


def test_valid_motor_command():
    command = SimulatedMotorController().command(50.0, "forward")
    assert MotorValidator().validate(command)


def test_invalid_motor_speed():
    with pytest.raises(ValueError, match="MOTOR_COMMAND_INVALID"):
        SimulatedMotorController().command(120.0, "forward")


def test_motor_controller_fault():
    with pytest.raises(RuntimeError, match="MOTOR_CONTROLLER_FAULT"):
        SimulatedMotorController(ready=False).command(20.0, "forward")
