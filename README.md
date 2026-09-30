# Robotic System Testing & Fault Detection Framework

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%20%7C%20Linux-lightgrey)
![Testing](https://img.shields.io/badge/Testing-pytest-green)
![CI](https://github.com/sohailkhadri4-design/Robotic-System-Testing-Fault-Detection-Framework/actions/workflows/tests.yml/badge.svg)

A Python-based **software test and fault-detection framework** for robotic subsystems. The project focuses on repeatable validation of sensor readings, motor commands, fault classification, logging, integration tests, and CI.

> **Verification boundary:** the current implementation uses deterministic simulated interfaces. It demonstrates automated software testing and fault injection; it does not claim physical robot test results.

## What the framework tests

- Sensor availability and reading validity
- Motor-command validity and controller faults
- Repeatable fault injection
- Fault classification
- Structured JSON-line logging
- Functional and integration tests
- Automated pytest execution through GitHub Actions

## System architecture

![System architecture](docs/system_architecture.svg)

The framework separates:
1. Test scenarios
2. Sensor and motor interfaces
3. Validation rules
4. Fault classification
5. Structured logging
6. Automated tests

This separation makes failures easier to reproduce and troubleshoot.

## Repository structure

```text
src/
├── sensors/
│   ├── sensor_manager.py
│   └── sensor_validator.py
├── motors/
│   ├── motor_controller.py
│   └── motor_validator.py
├── faults/
│   ├── fault_detector.py
│   └── fault_types.py
└── logging/
    └── test_logger.py

tests/
├── test_sensors.py
├── test_motor_control.py
├── test_fault_detection.py
└── test_integration.py

configs/
└── test_config.yaml

docs/
├── system_architecture.md
├── system_architecture.svg
├── test_plan.md
└── fault_scenarios.md

examples/
└── sample_test_run.py
```

## Quick start

```bash
git clone https://github.com/sohailkhadri4-design/Robotic-System-Testing-Fault-Detection-Framework.git
cd Robotic-System-Testing-Fault-Detection-Framework

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

PYTHONPATH=. python examples/sample_test_run.py
pytest -q
```

## Fault scenarios

| Scenario | Expected classification |
|---|---|
| Sensor unavailable | `SENSOR_UNAVAILABLE` |
| Out-of-range reading | `INVALID_SENSOR_READING` |
| Invalid motor command | `MOTOR_COMMAND_INVALID` |
| Motor controller unavailable | `MOTOR_CONTROLLER_FAULT` |

## Continuous integration

GitHub Actions is configured to install the Python dependencies and run `pytest -q` on pushes and pull requests targeting `main`.

The CI workflow is a **software-level verification step**. It should not be interpreted as proof of physical sensor or motor behavior.

## Why this project matters for embedded work

The project demonstrates a testing mindset around embedded systems:

- Define expected behavior before testing
- Reproduce failures deterministically
- Separate hardware interfaces from test logic
- Classify faults explicitly
- Record evidence for troubleshooting
- Automate regression checks

## Future hardware integration

The simulated interfaces can later be replaced with Raspberry Pi GPIO, I2C, SPI, PWM, and motor-driver adapters while retaining the higher-level validation and fault-detection layers.

Potential extensions:
- Hardware-in-the-loop testing
- Real sensor adapters
- Motor-driver integration
- Watchdog monitoring
- Test-report generation
- Additional CI checks

## License

MIT License. See [LICENSE](LICENSE).

## Author

**Syed Sohel Khadri**

Embedded Firmware | STM32 | ARM Cortex-M | Embedded C

GitHub: https://github.com/sohailkhadri4-design  
LinkedIn: https://www.linkedin.com/in/syed-sohel-khadri-7b570b381/
