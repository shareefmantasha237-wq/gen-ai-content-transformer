from abc import ABC, abstractmethod

class BaseGenerator(ABC):
    @abstractmethod
    async def generate(self, source: str, config: dict) -> str:
        pass
