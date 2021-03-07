import json

from .models import Device, Fan, FanControl, FanDiagnostic, FanInfo, FanSpeed, FanWifi
from .request import GET, PUT, request


async def get_info(device: Device, fan: Fan) -> FanInfo:
    response = await request(device, GET, f'/device/{fan.uid}')

    payload = response.payload.decode()
    data = json.loads(payload)
    return FanInfo.parse_obj(data)


async def get_control(device: Device, fan: Fan) -> FanControl:
    response = await request(device, GET, f'/control/{fan.uid}')

    payload = response.payload.decode()
    data = json.loads(payload)
    return FanControl.parse_obj(data)


async def get_wifi(device: Device, fan: Fan) -> FanWifi:
    response = await request(device, GET, f'/wifi/{fan.uid}')

    payload = response.payload.decode()
    data = json.loads(payload)
    # Returning the wifi password is not nice
    del data['client_passkey']
    return FanWifi.parse_obj(data)


async def get_diagnostic(device: Device, fan: Fan) -> FanDiagnostic:
    response = await request(device, GET, f'/diagnostic/{fan.uid}')

    payload = response.payload.decode()
    data = json.loads(payload)
    return FanDiagnostic.parse_obj(data)


async def set_time_remaining(
    device: Device, fan: Fan, time_remaining: int
) -> FanControl:
    response = await request(
        device, PUT, f'/control/{fan.uid}', {'remaining': time_remaining}
    )

    payload = response.payload.decode()
    data = json.loads(payload)
    return FanControl.parse_obj(data)


async def turn_on(device: Device, fan: Fan) -> FanControl:
    return await set_time_remaining(device, fan, 65535)


async def turn_off(device: Device, fan: Fan) -> FanControl:
    return await set_time_remaining(device, fan, 0)


async def set_speed(device: Device, fan: Fan, speed: FanSpeed) -> FanControl:

    response = await request(device, PUT, f'/control/{fan.uid}', {'speed': speed.value})

    payload = response.payload.decode()
    data = json.loads(payload)
    return FanControl.parse_obj(data)
