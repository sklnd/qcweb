from enum import Enum

from pydantic import BaseModel


class Device(BaseModel):
    ip: str


class Fan(BaseModel):
    uid: str


class FanSpeed(Enum):
    LOW = 1
    HIGH = 2


class FanInfo(BaseModel):
    uid: str
    type: int
    name: str
    version: str
    config: int
    model: str
    pincode: str
    role: int
    online: int
    status: int
    hubid: int


class FanWifi(BaseModel):
    uid: str
    version: str
    mac: str
    mode: int
    ssid: str
    ssid_broadcast: int
    client_ssid: str
    client_security: int
    dhcp: int
    ap_chan: int
    ipaddress: str
    ipsubnet: str
    dns: str
    gateway: str
    rssi: int


class FanDiagnostic(BaseModel):
    uid: str
    status: int
    life1: int
    life2: int
    life3: int
    relay1cycle: int
    relay2cycle: int
    relay3cycle: int


class FanControl(BaseModel):
    uid: str
    mode: int
    sequence: int
    speed: int
    duration: int
    started: int
    remaining: int
    source: int
    input_1_value: int
