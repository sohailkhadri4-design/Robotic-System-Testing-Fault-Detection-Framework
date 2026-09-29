# Test Plan

| ID | Test | Expected result |
|---|---|---|
| T01 | Valid sensor reading | PASS |
| T02 | Sensor unavailable | SENSOR_UNAVAILABLE |
| T03 | Out-of-range reading | INVALID_SENSOR_READING |
| T04 | Valid motor command | PASS |
| T05 | Invalid motor speed | MOTOR_COMMAND_INVALID |
| T06 | Motor controller unavailable | MOTOR_CONTROLLER_FAULT |
| T07 | Combined sensor/motor flow | PASS |

These are automated software tests using deterministic simulated interfaces. They are not physical robot test results.
