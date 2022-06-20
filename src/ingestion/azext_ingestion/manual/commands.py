# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
#from azext_ingestion.generated._client_factory import cf_ingestion, cf_validation

def load_command_table(self, _):

    # TODO: Add command type here
    # ingestion_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_ingestion)

    # This is the main command group az ingestion
    with self.command_group('ingestion') as g:
        pass
        #g.custom_command('create', 'create_ingestion')
        # g.command('delete', 'delete')
        #g.custom_command('list', 'list_ingestion')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_ingestion')

    with self.command_group('ingestion', is_preview=True):
        pass

    ############################################
    # Token
    ############################################

    # This is a sub command group az ingestion token that takes in a client factory which will 
    # produce the correct validation object for the inputs. 
    from azext_ingestion.manual._client_factory import cf_token_get
    with self.command_group('ingestion token',client_factory=cf_token_get, is_experimental=True) as g:
        g.custom_command('get', 'get_token')

    with self.command_group('ingestion token', is_preview=True):
        pass

    ############################################
    # Platform Configuration
    ############################################
    from azext_ingestion.manual._client_factory import cf_platform_config
    with self.command_group('ingestion platform',client_factory=cf_platform_config, is_experimental=True) as g:
        g.custom_command('add', 'add_platform')
        g.custom_command('list', 'list_platforms')
        g.custom_command('remove', 'remove_platform')
        g.custom_command('show', 'show_platform')

    with self.command_group('ingestion platform', is_preview=True):
        pass

    ############################################
    # Tool Configuration
    ############################################
    from azext_ingestion.manual._client_factory import cf_tool_config
    with self.command_group('ingestion tool',client_factory=cf_tool_config, is_experimental=True) as g:
        g.custom_command('add', 'add_tool')
        g.custom_command('list', 'list_tools')
        g.custom_command('remove', 'remove_tool')
        g.custom_command('show', 'show_tool')

    with self.command_group('ingestion tool', is_preview=True):
        pass

    ############################################
    # Tool Execution Configuration
    ############################################
    from azext_ingestion.manual._client_factory import cf_tool_executor
    with self.command_group('ingestion execute',client_factory=cf_tool_executor, is_experimental=True) as g:
        g.custom_command('job', 'execute_tool')

    with self.command_group('ingestion execute', is_preview=True):
        pass
