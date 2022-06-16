# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_ingestion._client_factory import cf_ingestion


def load_command_table(self, _):

    # TODO: Add command type here
    # ingestion_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_ingestion)


    with self.command_group('ingestion') as g:
        g.custom_command('token', 'get_token')
        g.custom_command('create', 'create_ingestion')
        # g.command('delete', 'delete')
        g.custom_command('list', 'list_ingestion')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_ingestion')


    with self.command_group('ingestion', is_preview=True):
        pass

