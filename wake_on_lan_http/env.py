"""Environment variables."""
import os

DEVICES_FILE = os.environ.get("DEVICES_FILE", "devices.json")
PING_TIMEOUT_SECONDS = int(os.environ.get("PING_TIMEOUT_SECONDS", "1"))
