from logging import Logger
from typing import Sequence
from ..models import DeviceAttributes, Type
from .api import IpLink


def createIpLinkMock(logger: Logger) -> IpLink:

    class IpLinkMock(IpLink):

        def show(self, name: str = None, group: str = None, up: bool = None, master: str = None, vrf: str = None, type: Type = None) -> Sequence[DeviceAttributes]:
            return [DeviceAttributes(name=name)]

    return IpLinkMock()
