from pydantic import BaseModel


class Device(BaseModel):
    ip: str


class Endpoint(BaseModel):
    uid: str
