import json
from logging import log
from typing import List

from aiocoap import GET, PUT, Context, Message

from .models import Device, Endpoint


async def request(device: Device, method: any, endpoint: str):
    protocol = await Context.create_client_context()
    request = Message(code=method, uri=f'coap://{device.ip}{endpoint}')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        log.error('Failed to fetch resource: %s', e)
        raise

    if not response.code.is_successful():
        log.error('Invalid response to endpoint %s: %s', endpoint, e)
        raise ValueError('Invalid response', response)

    return response


async def list(device: Device) -> List[Endpoint]:

    response = await request(device, GET, '/uids')

    payload = response.payload.decode()
    data = json.loads(payload)

    return [Endpoint.parse_obj(e) for e in data]
