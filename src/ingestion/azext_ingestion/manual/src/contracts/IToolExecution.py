# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class IToolExecution(ABC):
    @abstractmethod
    def execute(
        self, 
        authentication_token:str, 
        platform:dict, 
        tool:dict, 
        job_configuration:str
    ):
        """prepare environment for acquisition"""

