from abc import ABC, abstractmethod


class KeyboardMethod(ABC):

    @abstractmethod
    def __call__(self, key: str) -> bool:
        pass
