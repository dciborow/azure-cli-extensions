# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_ingestion.manual.src.contracts.ITokenProvider import ITokenProvider

def cf_ingestion(cli_ctx, *_):
    """
    Default ingestion client currently unused.
    """

    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    # TODO: Replace CONTOSO with the appropriate label and uncomment
    # from azure.mgmt.CONTOSO import CONTOSOManagementClient
    # return get_mgmt_service_client(cli_ctx, CONTOSOManagementClient)
    return None

def cf_token_get(cli_ctx, *_) -> ITokenProvider:
    """
    Client for acquiring a token. 
    """

    # Required /seen that it's a tuple with 1 item, first item is 
    #{
	#   'cmd': < azure.cli.core.commands.AzCliCommand object at 0x0000022F1E49CFC8 > ,
	#   'param_name': None,
	#   'param_name2': None,
	#   'etc....': None
    #}
    from .src._sp_token_provider import SPTokenConfigurationService
    return SPTokenConfigurationService()

    # There is a lot of stuff in this context object, how do we get the 
#    for k in cli_ctx.__dict__:
#        print(k, cli_ctx.__dict__[k], "\n")
