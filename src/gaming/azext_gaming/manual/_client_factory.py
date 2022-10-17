# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_gaming.manual.src.contracts.IDDCProvider import IDDCProvider
from azext_gaming.manual.src.contracts.ISPTokenProvider import ISPTokenProvider
from azext_gaming.manual.src.contracts.IUserTokenProvider import IUserTokenProvider
from azext_gaming.manual.src._token_user_provider import CliUserInfo

from azext_gaming.manual.src.contracts.IPersistConfiguration import IPersistConfiguration
from azext_gaming.manual.src._tool_executioner import ToolExecutionContext, ToolExecutioner

def cf_gaming(cli_ctx, *_):
    """
    Default gaming client currently unused.
    """

    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    # TODO: Replace CONTOSO with the appropriate label and uncomment
    # from azure.mgmt.CONTOSO import CONTOSOManagementClient
    # return get_mgmt_service_client(cli_ctx, CONTOSOManagementClient)
    return None


def cf_ddc_get(cli_ctx, *_) -> IDDCProvider:
    """
    Client for acquiring a user or platform token. 
    """
    from .src._ddc_provider import DDCProvider
    client_info = CliUserInfo(cli_ctx)
    return DDCProvider(client_info)

def cf_usertoken_get(cli_ctx, *_) -> IUserTokenProvider:
    """
    Client for acquiring a user or platform token. 
    """
    from .src._token_user_provider import UserTokenProvider
    client_info = CliUserInfo(cli_ctx)
    return UserTokenProvider(client_info)

def cf_sptoken_get(cli_ctx, *_) -> ISPTokenProvider:
    """
    Client for acquiring a service principal token. 
    """
    from .src._token_sp_token import SPTokenConfigurationService
    return SPTokenConfigurationService()

def cf_platform_config(cli_ctx, *_) -> IPersistConfiguration:
    """
    Client for persisting platform configurations
    """
    from .src._persist_osdu_config import OSDUPersistConfiguration
    return OSDUPersistConfiguration()

def cf_utility_config(cli_ctx, *_) -> IPersistConfiguration:
    """
    Client for persisting tool configurations
    """
    from .src._persist_utility_config import UtilityPersistConfiguration
    return UtilityPersistConfiguration()

def cf_tool_executor_example(cli_ctx, *_) -> ToolExecutionContext:
    """
    Client holding the selected tool and platform configuration data along with an 
    executor IToolExecution

    For executioner provide the right execution class for the task you are trying to 
    achieve. This is a simple example job executioner, but if we start wrapping all kinds 
    of external tools this will be required to be different. 
    """
    context = ToolExecutionContext()
    context.executor = ToolExecutioner()
    context.platform_config = cf_platform_config(None, None)
    context.tool_config = cf_utility_config(None, None)
    return context