# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_ingestion.manual.src.contracts.ISPTokenProvider import ISPTokenProvider
from azext_ingestion.manual.src.contracts.IUserTokenProvider import IUserTokenProvider
from azext_ingestion.manual.src._user_token_provider import CliUserInfo

from azext_ingestion.manual.src.contracts.IPersistConfiguration import IPersistConfiguration
from azext_ingestion.manual.src._tool_executioner import ToolExecutionContext, ToolExecutioner
def cf_ingestion(cli_ctx, *_):
    """
    Default ingestion client currently unused.
    """

    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    # TODO: Replace CONTOSO with the appropriate label and uncomment
    # from azure.mgmt.CONTOSO import CONTOSOManagementClient
    # return get_mgmt_service_client(cli_ctx, CONTOSOManagementClient)
    return None

def cf_usertoken_get(cli_ctx, *_) -> IUserTokenProvider:
    """
    Client for acquiring a user or platform token. 
    """
    from .src._user_token_provider import UserTokenProvider
    client_info = CliUserInfo(cli_ctx)
    return UserTokenProvider(client_info)

def cf_sptoken_get(cli_ctx, *_) -> ISPTokenProvider:
    """
    Client for acquiring a service principal token. 
    """
    from .src._sp_token_provider import SPTokenConfigurationService
    return SPTokenConfigurationService()

def cf_platform_config(cli_ctx, *_) -> IPersistConfiguration:
    """
    Client for persisting platform configurations
    """
    from .src._osdu_persist_config import OSDUPersistConfiguration
    return OSDUPersistConfiguration()

def cf_utility_config(cli_ctx, *_) -> IPersistConfiguration:
    """
    Client for persisting tool configurations
    """
    from .src._utility_persist_config import UtilityPersistConfiguration
    return UtilityPersistConfiguration()

def cf_tool_executor(cli_ctx, *_) -> ToolExecutionContext:
    """
    Client holding the selected tool and platform configuration data along with an 
    executor IToolExecution
    """
    context = ToolExecutionContext()
    context.executor = ToolExecutioner()
    context.platform_config = cf_platform_config(None, None)
    context.tool_config = cf_utility_config(None, None)
    return context