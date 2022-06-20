# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class ITokenProvider(ABC):
    @abstractmethod
    def prepare(self, tenent, principal, credential, configuration):
        """prepare environment for acquisition"""

    @abstractmethod
    def acquire_token(self) -> dict:
        """get a token"""