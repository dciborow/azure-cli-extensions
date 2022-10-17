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
        #g.custom_command('create', 'create_gaming')
        # g.command('delete', 'delete')
        #g.custom_command('list', 'list_gaming')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_gaming')

    with self.command_group('{}'.format(CommandConstants.ROOT), is_preview=True):
        pass

    ############################################
    # Token
    ############################################

    # Command for getting a service principal token (usable with platform or whatever.)
    from azext_gaming.manual._client_factory import cf_sptoken_get
    with self.command_group('{} auth'.format(CommandConstants.ROOT),client_factory=cf_sptoken_get, is_experimental=True) as g:
        g.custom_command('sp', 'get_token')

    # Commands for getting token for user (restricted to Azure Resources) or platform which takes
    # a users refresh token and provides a token to use with the platform. 
    from azext_gaming.manual._client_factory import cf_usertoken_get
    with self.command_group('{} auth'.format(CommandConstants.ROOT),client_factory=cf_usertoken_get, is_experimental=True) as g:
        g.custom_command('user', 'get_user_token')
        g.custom_command('platform', 'get_platform_token')

    with self.command_group('{} auth'.format(CommandConstants.ROOT), is_preview=True):
        pass

    ############################################
    # Platform Configuration
    ############################################
    from azext_gaming.manual._client_factory import cf_platform_config
    with self.command_group('{} platform'.format(CommandConstants.ROOT),client_factory=cf_platform_config, is_experimental=True) as g:
        g.custom_command('add', 'add_platform')
        g.custom_command('list', 'list_platforms')
        g.custom_command('remove', 'remove_platform')
        g.custom_command('show', 'show_platform')

    with self.command_group('{} platform'.format(CommandConstants.ROOT), is_preview=True):
        pass

    ############################################
    # Tool Configuration
    ############################################
    from azext_gaming.manual._client_factory import cf_utility_config
    with self.command_group('{} utility'.format(CommandConstants.ROOT),client_factory=cf_utility_config, is_experimental=True) as g:
        g.custom_command('add', 'add_utility')
        g.custom_command('list', 'list_utility')
        g.custom_command('remove', 'remove_utility')
        g.custom_command('show', 'show_utility')

    with self.command_group('{} utility'.format(CommandConstants.ROOT), is_preview=True):
        pass

    ############################################
    # Tool Execution Configuration
    ############################################
    from azext_gaming.manual._client_factory import cf_tool_executor_example
    with self.command_group('{} execute'.format(CommandConstants.ROOT),client_factory=cf_tool_executor_example, is_experimental=True) as g:
        g.custom_command('job', 'execute_utility')

    with self.command_group('{} execute'.format(CommandConstants.ROOT), is_preview=True):
        pass
