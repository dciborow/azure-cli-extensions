# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_gaming.manual._help import helps  # pylint: disable=unused-import


class GamingCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_gaming.manual._client_factory import cf_gaming
        gaming_custom = CliCommandType(
            operations_tmpl='azext_gaming.custom#{}',
            client_factory=cf_gaming)
        super(GamingCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                  custom_command_type=gaming_custom)

    def load_command_table(self, args):
        from azext_gaming.manual.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_gaming.manual._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = GamingCommandsLoader
