from logging import Logger
from typing import Sequence
from ..models import DeviceAttributes, Type
from .api import IpLink


def createIpLinkShell(logger: Logger) -> IpLink:

    class IpLinkShell(IpLink):

        def show(self, name: str = None, group: str = None, up: bool = None, master: str = None, vrf: str = None, type: Type = None) -> Sequence[DeviceAttributes]:
            logger.error('Not implemented yet')
            return []

    return IpLinkShell()
