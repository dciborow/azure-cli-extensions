# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class IResourceProvider(ABC):
    @abstractmethod
    def create(self, location, resource_group_name, name) -> dict:
        """create ddc"""

    @abstractmethod
    def list(self, location, resource_group_name) -> dict:
        """list ddc"""
