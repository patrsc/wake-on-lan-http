"""Core functions."""
import os
import json
from dataclasses import dataclass
from wakeonlan import send_magic_packet

@dataclass
class Device:
    """Represents a device."""
    id: str
    name: str
    mac: str
    host: str
    user: str
    id_file: str


def start(device: Device) -> None:
    """Start a device using Wake On LAN."""
    send_magic_packet(device.mac)


def is_online(device: Device, timeout=1) -> bool:
    """Check if a device is online using ping."""
    command = f"ping -c 1 -W {timeout} {device.host} >/dev/null 2>/dev/null"
    exit_code = os.system(command)
    return exit_code == 0


def shutdown(device: Device) -> None:
    """Shutdown a device using SSH."""
    command = f"ssh -i '{device.id_file}' {device.user}@{device.host} 'sudo shutdown -P now'"
    exit_code = os.system(command)
    if exit_code != 0:
        raise ValueError(f"ssh shutdown returned non-zero exit code: {exit_code}")


def read_devices(device_file) -> dict[str, Device]:
    """Read devices from file and put them into a dict id->Device."""
    with open(device_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {item["id"]: Device(**item) for item in data}
