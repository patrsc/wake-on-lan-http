"""CLI interface."""
import sys
from .core import read_devices, start, shutdown, is_online
from .env import DEVICES_FILE, PING_TIMEOUT_SECONDS


def cli_main():
    """CLI main function."""
    device_id = sys.argv[1]
    action = sys.argv[2]
    devices = read_devices(DEVICES_FILE)
    device = devices[device_id]
    if action == "on":
        start(device)
    elif action == "off":
        shutdown(device)
    elif action == "state":
        state = "on" if is_online(device, timeout=PING_TIMEOUT_SECONDS) else "off"
        print(state)
    else:
        raise ValueError("unknown action")
