# System Architecture

The framework is organized into device interfaces, validation, fault detection, and test/logging layers.

1. Device interfaces expose sensor and motor operations.
2. Validation checks readings and commands against constraints.
3. Fault detection converts failures into typed fault events.
4. Tests exercise normal and fault conditions while structured logging records events.

The simulated interfaces keep the project deterministic and portable. Real Raspberry Pi GPIO, I2C, SPI, PWM, and motor-driver adapters can be added behind the same high-level interfaces.
