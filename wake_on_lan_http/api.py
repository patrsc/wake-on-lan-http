"""REST API."""
from typing import Annotated, Literal

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .core import read_devices, start, shutdown, is_online, Device
from .env import DEVICES_FILE, PING_TIMEOUT_SECONDS

devices = read_devices(DEVICES_FILE)
app = FastAPI(title="Wake on LAN HTTP API")

class DeviceState(BaseModel):
    """Device state."""
    state: Literal["off", "on"]


def get_device(device: str) -> Device:
    "Get device by id."
    try:
        return devices[device]
    except KeyError as e:
        raise HTTPException(status_code=404, detail="Device not found") from e


@app.get("/", include_in_schema=False)
def read_root():
    """Root web interface."""
    return FileResponse("index.html")


@app.get("/devices")
def get_devices() -> list[Device]:
    """Get devices."""
    return list(devices.values())


@app.get("/devices/{device}/state")
def get_device_state(device: Annotated[Device, Depends(get_device)]) -> DeviceState:
    """Get device state."""
    return DeviceState(
        state="on" if is_online(device, timeout=PING_TIMEOUT_SECONDS) else "off",
    )


@app.put("/devices/{device}/on", status_code=204)
def turn_device_on(device: Annotated[Device, Depends(get_device)]) -> None:
    """Turn device on."""
    start(device)


@app.put("/devices/{device}/off", status_code=204)
def turn_device_off(device: Annotated[Device, Depends(get_device)]) -> None:
    """Turn device off."""
    shutdown(device)
