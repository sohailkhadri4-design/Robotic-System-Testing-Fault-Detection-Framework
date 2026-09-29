from dataclasses import dataclass


@dataclass
class MotorCommand:
    speed_percent: float
    direction: str


class SimulatedMotorController:
    """Deterministic motor interface for development and automated tests."""

    VALID_DIRECTIONS = {"forward", "reverse", "stop"}

    def __init__(self, ready: bool = True):
        self.ready = ready
        self.last_command = MotorCommand(0.0, "stop")

    def command(self, speed_percent: float, direction: str) -> MotorCommand:
        if not self.ready:
            raise RuntimeError("MOTOR_CONTROLLER_FAULT")
        if not 0.0 <= speed_percent <= 100.0:
            raise ValueError("MOTOR_COMMAND_INVALID")
        if direction not in self.VALID_DIRECTIONS:
            raise ValueError("MOTOR_COMMAND_INVALID")
        self.last_command = MotorCommand(speed_percent, direction)
        return self.last_command
