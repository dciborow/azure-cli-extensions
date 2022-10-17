# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_gaming.manual.src.contracts.IResourceProvider import IResourceProvider
from azext_gaming.manual.src._token_user_provider import CliUserInfo



def cf_gaming(cli_ctx, *_):
    """
    Default gaming client currently unused.
    """

    from azure.cli.core.commands.client_factory import get_mgmt_service_client

    # TODO: Replace CONTOSO with the appropriate label and uncomment
    # from azure.mgmt.CONTOSO import CONTOSOManagementClient
    # return get_mgmt_service_client(cli_ctx, CONTOSOManagementClient)
    return None


def cf_gdvm(cli_ctx, *_) -> IResourceProvider:
    """
    Client for acquiring a user or platform token.
    """
    from .src._resource_provider import ResourceProvider

    client_info = CliUserInfo(cli_ctx)
    return ResourceProvider(client_info)


def cf_ddc_get(cli_ctx, *_) -> IResourceProvider:
    """
    Client for acquiring a user or platform token.
    """
    from .src._resource_provider import ResourceProvider

    client_info = CliUserInfo(cli_ctx)
    return ResourceProvider(client_info)


def cf_pixel_streaming(cli_ctx, *_) -> IResourceProvider:
    """
    Client for acquiring a user or platform token.
    """
    from .src._resource_provider import ResourceProvider

    client_info = CliUserInfo(cli_ctx)
    return ResourceProvider(client_info)
