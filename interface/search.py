

from abc import ABC, abstractmethod


class ISearch(ABC):

    @abstractmethod
    def search(self):
        pass
