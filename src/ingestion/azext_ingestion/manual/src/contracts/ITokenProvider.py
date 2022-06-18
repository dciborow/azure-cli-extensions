from abc import ABC, abstractmethod


class ITokenProvider(ABC):
    @abstractmethod
    def prepare(self, tenent, principal, credential, configuration):
        """prepare environment for acquisition"""

    def acquire_token(self) -> dict:
        """get a token"""