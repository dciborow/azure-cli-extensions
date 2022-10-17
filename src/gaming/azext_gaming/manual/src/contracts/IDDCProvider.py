# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class IDDCProvider(ABC):
    @abstractmethod
    def create(self) -> dict:
        """create ddc"""

    @abstractmethod
    def list(self) -> dict:
        """list ddc"""
