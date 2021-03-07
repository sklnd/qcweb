from typing import List

from fastapi import APIRouter
from pydantic.main import BaseModel

from ..qc import endpoints, fan
from ..qc.models import Device, Fan, FanControl
from ..settings import settings

router = APIRouter()


class FanListResponse(BaseModel):
    fans: List[Fan]


class FanControlResponse(BaseModel):
    control: FanControl


@router.get("/fan/list", tags=["fans"], response_model=FanListResponse)
async def list_fans():
    device = Device(ip=settings.quiet_cool_device)
    fans = await endpoints.list(device)
    return {"fans": fans}


@router.post("/fan/{fan_id}/turn_on", tags=["fans"], response_model=FanControlResponse)
async def turn_on(fan_id):
    device = Device(ip=settings.quiet_cool_device)
    fan_obj = Fan(uid=fan_id)
    control = await fan.turn_on(device, fan_obj)
    return {'control': control}


@router.post("/fan/{fan_id}/turn_off", tags=["fans"], response_model=FanControlResponse)
async def turn_off(fan_id):
    device = Device(ip=settings.quiet_cool_device)
    fan_obj = Fan(uid=fan_id)
    control = await fan.turn_off(device, fan_obj)
    return {'control': control}
