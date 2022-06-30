# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class IUserTokenProvider(ABC):
    @abstractmethod
    def acquire_token(self, scope:str) -> dict:
        """get a token"""

    @abstractmethod
    def acquire_platform_token(self, refresh_token:str, client_id:str, dev_portal:str) -> dict:
        """get a token"""        