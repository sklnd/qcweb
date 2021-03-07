import json
from logging import log
from typing import Dict, Optional

from aiocoap import GET, PUT, Context, Message

from .models import Device


async def request(
    device: Device, method: any, endpoint: str, payload: Optional[Dict] = None
):
    payload_bytes = b''
    if payload:
        payload_bytes = json.dumps(payload).encode()

    protocol = await Context.create_client_context()
    request = Message(
        code=method, uri=f'coap://{device.ip}{endpoint}', payload=payload_bytes
    )

    try:
        response = await protocol.request(request).response
    except Exception as e:
        log.error('Failed to fetch resource: %s', e)
        raise

    if not response.code.is_successful():
        log.error('Invalid response to endpoint %s: %s', endpoint, e)
        raise ValueError('Invalid response', response)

    return response
