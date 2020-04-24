from ..iplink import IpLink, DeviceAttributes
from typing import Sequence


def show_devices(iplink: IpLink) -> Sequence[DeviceAttributes]:
    return iplink.show()


def show_device(iplink: IpLink, name: str) -> DeviceAttributes:
    result = iplink.show(name = name)
    return result[0]
