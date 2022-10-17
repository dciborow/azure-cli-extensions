# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType
from azext_energy.command_const import CommandConstants
from ._validators import acquire_token_validator, configuration_file_validator


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    energy_name_type = CLIArgumentType(options_list='--energy-name-name', help='Name of the energy.', id_part='name')

    configuration_file_type = CLIArgumentType(options_list='--energy-configuration-file', help='Configuration File', id_part='file', required=False)

    # Service Principal
    energy_auth_type = CLIArgumentType(options_list='--energy-auth-sp', help='Service Principal ID.', id_part='sp', required=False)
    energy_auth_secret_type = CLIArgumentType(options_list='--energy-auth-secret', help='Service Principal Secret.', id_part='secret', required=False)
    energy_auth_tenent_type = CLIArgumentType(options_list='--energy-auth-tenent', help='Active Directory Tenent', id_part='tenent', required=False)

    # User
    energy_auth_scope_type = CLIArgumentType(options_list='--energy-auth-scope', help='Authentication Scope', id_part='scope', required=True)

    # Platform - alsu uses energy auth type
    energy_auth_refresh_type = CLIArgumentType(options_list='--energy-auth-refresh', help='User Refersh token', id_part='refresh', required=True)
    energy_auth_portal_type = CLIArgumentType(options_list='--energy-auth-platform', help='Experience Lab Portal Url', id_part='platform', required=True)


    configuration_section_platform = CLIArgumentType(options_list='--energy-configuration-platform', help='Configuration Platform', id_part='platform', required=True)
    configuration_section_tool = CLIArgumentType(options_list='--energy-configuration-tool', help='Configuration Tool', id_part='tool', required=True)

    # Main command group parameters - global currently unused
    with self.argument_context(f'{CommandConstants.ROOT}') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('energy_name', energy_name_type, options_list=['--name', '-n'])

    with self.argument_context(f'{CommandConstants.ROOT} list') as c:
        c.argument('energy_name', energy_name_type, id_part=None)

    ##############################################
    # Token
    ##############################################

    # Set up parameters for a sub group, uses a validator to ensure we either get what we need
    # from the command line OR have a valid configuration file (file anyway, checked internally)
    with self.argument_context(f'{CommandConstants.ROOT} auth sp', validator=acquire_token_validator) as c:
        c.argument('service_principal', energy_auth_type, options_list=['--service-principal', '-sp'])
        c.argument('service_principal_secret', energy_auth_secret_type, options_list=['--service-principal-credential', '-c'])
        c.argument('azure_tenent', energy_auth_tenent_type, options_list=['--tenent', '-t'])
        c.argument('configuration_file', configuration_file_type, options_list=['--configuration', '-f'])

    with self.argument_context(f'{CommandConstants.ROOT} auth user') as c:
        c.argument('scope', energy_auth_scope_type, options_list=['--scope', '-sc'])

    with self.argument_context(f'{CommandConstants.ROOT} auth platform') as c:
        c.argument('service_principal', energy_auth_type, options_list=['--service-principal', '-sp'])
        c.argument('dev_platform', energy_auth_type, options_list=['--dev-portal', '-dp'])
        c.argument('refresh_token', energy_auth_type, options_list=['--refresh-token', '-rt'])

    ##############################################
    # Platform Config
    ##############################################
    with self.argument_context(f'{CommandConstants.ROOT} platform add', validator=configuration_file_validator) as c:
        c.argument('configuration_file', configuration_file_type, options_list=['--configuration', '-f'])

    with self.argument_context(f'{CommandConstants.ROOT} platform show') as c:
        c.argument('platform_name', configuration_section_platform, options_list=['--name', '-n'])

    with self.argument_context(f'{CommandConstants.ROOT} platform remove') as c:
        c.argument('platform_name', configuration_section_platform, options_list=['--name', '-n'])

    ##############################################
    # Tool Config
    ##############################################
    with self.argument_context(f'{CommandConstants.ROOT} utility add', validator=configuration_file_validator) as c:
        c.argument('configuration_file', configuration_file_type, options_list=['--configuration', '-f'])

    with self.argument_context(f'{CommandConstants.ROOT} utility show') as c:
        c.argument('utility_name', configuration_section_tool, options_list=['--name', '-n'])

    with self.argument_context(f'{CommandConstants.ROOT} utility remove') as c:
        c.argument('utility_name', configuration_section_tool, options_list=['--name', '-n'])

    ##############################################
    # Tool Execute
    ##############################################
    with self.argument_context(f'{CommandConstants.ROOT} execute', validator=configuration_file_validator) as c:
        c.argument('platform_name', configuration_section_platform, options_list=['--platform', '-p'])
        c.argument('utility_name', configuration_section_tool, options_list=['--utility', '-u'])
        c.argument('configuration_file', configuration_file_type, options_list=['--configuration', '-f'])
