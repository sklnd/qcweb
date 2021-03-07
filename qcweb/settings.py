from pydantic import BaseSettings


class Settings(BaseSettings):
    quiet_cool_device: str = "10.0.0.2"
    debug: bool = True


settings = Settings()
