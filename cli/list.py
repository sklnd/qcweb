from qcweb.qc.endpoints import list
from qcweb.qc.models import Device
import asyncio


async def main():
    device = Device(ip="10.0.128.65")

    result = await list(device)
    print(result)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
