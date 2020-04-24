import abc
from typing import Sequence
from ..models import DeviceAttributes, Type


class IpLink(abc.ABC):

    @abc.abstractmethod
    def show(self, name: str = None, group: str = None, up: bool = None, master: str = None, vrf: str = None, type: Type = None) -> Sequence[DeviceAttributes]:
        pass
