from .motor_controller import MotorCommand


class MotorValidator:
    def __init__(self, max_speed_percent: float = 100.0):
        self.max_speed_percent = max_speed_percent

    def validate(self, command: MotorCommand) -> bool:
        return (
            0.0 <= command.speed_percent <= self.max_speed_percent
            and command.direction in {"forward", "reverse", "stop"}
        )
