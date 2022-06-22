# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .contracts.IToolExecution import IToolExecution
from .contracts.IPersistConfiguration import IPersistConfiguration

class ToolExecutionContext:
    def __init__(self):
        self.platform_config:IPersistConfiguration = None
        self.tool_config:IPersistConfiguration = None
        self.executor:IToolExecution = None

class ToolExecutioner(IToolExecution):

    def __init__(self):
        self.status = None


    def execute(
            self, 
            authentication_token:str, 
            platform:dict, 
            utility:dict, 
            job_configuration:dict
        ):
        """
        Execute the tool 
        """    
        print("Executing Job")
        print("Token:", authentication_token)
        print("Platform:", platform)
        print("Utility:", utility)
        print("Job:", job_configuration)                        