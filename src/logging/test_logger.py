import json
import logging
from datetime import datetime, timezone


class StructuredTestLogger:
    def __init__(self, name: str = "robotic-test-framework"):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(message)s"))
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def event(self, event: str, **fields) -> None:
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": event,
            **fields,
        }
        self.logger.info(json.dumps(payload, sort_keys=True))
