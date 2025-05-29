"""Wake on LAN CLI interface.

Usage: python cli.py DEVICE ACTION
where DEVICE is the device ID from devices.json
and ACTION is on, off, or state
"""
from wake_on_lan_http.cli import cli_main


if __name__ == "__main__":
    cli_main()
