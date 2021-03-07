import json
from typing import List

from aiocoap import GET

from .models import Device, Fan
from .request import request


async def list(device: Device) -> List[Fan]:

    response = await request(device, GET, '/uids')

    payload = response.payload.decode()
    data = json.loads(payload)

    return [Fan.parse_obj(e) for e in data]


async def list_endpoints(device: Device):
    response = await request(device, GET, '/.well-known/core')

    payload = response.payload.decode()
    data = payload.decode()
    return data
