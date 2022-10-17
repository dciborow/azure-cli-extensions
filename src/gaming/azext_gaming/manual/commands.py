# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_gaming.command_const import CommandConstants

def load_command_table(self, _):

    # TODO: Add command type here
    # gaming_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_gaming)

    # This is the main command group az gaming
    with self.command_group('{}'.format(CommandConstants.ROOT)) as g:
        pass
        # g.custom_command('create', 'create_gaming')
        # g.command('delete', 'delete')
        # g.custom_command('list', 'list_gaming')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_gaming')

    with self.command_group('{}'.format(CommandConstants.ROOT), is_preview=True):
        pass

    ############################################
    # Unreal Cloud DDC Configuration
    ############################################
    from azext_gaming.manual._client_factory import cf_ddc_get, cf_gdvm, cf_pixel_streaming
    with self.command_group('{} gdvm'.format(CommandConstants.ROOT),client_factory=cf_gdvm, is_experimental=True) as g:
        g.custom_command('create', 'create_gdvm')
        g.custom_command('list', 'list_gdvm')

    with self.command_group('{} unreal-cloud ddc'.format(CommandConstants.ROOT), client_factory=cf_ddc_get, is_experimental=True) as g:
        g.custom_command('create', 'create_ddc')
        g.custom_command('list', 'list_ddc')

    with self.command_group('{} unreal-cloud pixel-streaming'.format(CommandConstants.ROOT),client_factory=cf_pixel_streaming, is_experimental=True) as g:
        g.custom_command('create', 'create_pixel_streaming')
        g.custom_command('list', 'list_pixel_streaming')
