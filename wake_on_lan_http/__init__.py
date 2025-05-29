"""Wake on LAN."""
from .core import Device, start, shutdown, is_online, read_devices

__all__ = ["Device", "start", "shutdown", "is_online", "read_devices"]
