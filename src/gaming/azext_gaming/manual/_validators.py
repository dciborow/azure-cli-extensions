# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
from knack.util import CLIError


def example_name_or_id_validator(cmd, namespace):
    # Example of a storage account name or ID validator.
    # See: https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#supporting-name-or-id-parameters
    from azure.cli.core.commands.client_factory import get_subscription_id
    from msrestazure.tools import is_valid_resource_id, resource_id

    if namespace.storage_account:
        if not is_valid_resource_id(namespace.RESOURCE):
            namespace.storage_account = resource_id(
                subscription=get_subscription_id(cmd.cli_ctx),
                resource_group=namespace.resource_group_name,
                namespace="Microsoft.Storage",
                type="storageAccounts",
                name=namespace.storage_account,
            )


# For az gaming auth sp, validate the parameters
def acquire_token_validator(cmd, namespace):
    """
    Must provide service_principal, service_principal_secret, azure_tenent together
    or have a valid configuration_file
    """
    if not namespace.service_principal or not namespace.service_principal_secret or not namespace.azure_tenent:
        # Then there MUST be a valid configuration file present.
        if not namespace.configuration_file:
            raise CLIError("Call requires valid configuration information, see help for the command.")

        if not os.path.exists(namespace.configuration_file):
            raise CLIError("Provided configuration file does not exist.")


def configuration_file_validator(cmd, namespace):
    """
    Must provide service_principal, service_principal_secret, azure_tenent together
    or have a valid configuration_file
    """
    if not namespace.configuration_file:
        raise CLIError("Call requires valid configuration information, see help for the command.")

    if not os.path.exists(namespace.configuration_file):
        raise CLIError("Provided configuration file does not exist.")
