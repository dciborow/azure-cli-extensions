# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType
from ._validators import acquire_token_validator, configuration_file_validator


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    ingestion_name_type = CLIArgumentType(options_list='--ingestion-name-name', help='Name of the Ingestion.', id_part='name')

    configuration_file_type = CLIArgumentType(options_list='--ingestion-configuration-file', help='Configuration File', id_part='file', required=False)

    # Service Principal
    ingestion_auth_type = CLIArgumentType(options_list='--ingestion-auth-sp', help='Service Principal ID.', id_part='sp', required=False)
    ingestion_auth_secret_type = CLIArgumentType(options_list='--ingestion-auth-secret', help='Service Principal Secret.', id_part='secret', required=False)
    ingestion_auth_tenent_type = CLIArgumentType(options_list='--ingestion-auth-tenent', help='Active Directory Tenent', id_part='tenent', required=False)
    
    # User
    ingestion_auth_scope_type = CLIArgumentType(options_list='--ingestion-auth-scope', help='Authentication Scope', id_part='scope', required=True)

    # Platform - alsu uses ingestion auth type
    ingestion_auth_refresh_type = CLIArgumentType(options_list='--ingestion-auth-refresh', help='User Refersh token', id_part='refresh', required=True)
    ingestion_auth_portal_type = CLIArgumentType(options_list='--ingestion-auth-platform', help='Experience Lab Portal Url', id_part='platform', required=True)


    configuration_section_platform = CLIArgumentType(options_list='--ingestion-configuration-platform', help='Configuration Platform', id_part='platform', required=True)
    configuration_section_tool = CLIArgumentType(options_list='--ingestion-configuration-tool', help='Configuration Tool', id_part='tool', required=True)

    # Main command group parameters - global currently unused
    with self.argument_context('ingestion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('ingestion_name', ingestion_name_type, options_list=['--name', '-n'])

    with self.argument_context('ingestion list') as c:
        c.argument('ingestion_name', ingestion_name_type, id_part=None)

    ##############################################
    # Token
    ##############################################

    # Set up parameters for a sub group, uses a validator to ensure we either get what we need
    # from the command line OR have a valid configuration file (file anyway, checked internally)
    with self.argument_context('ingestion auth sp', validator=acquire_token_validator) as c:
        c.argument('service_principal', ingestion_auth_type, options_list=['--service-principal', '-sp'])
        c.argument('service_principal_secret', ingestion_auth_secret_type, options_list=['--service-principal-credential', '-c'])
        c.argument('azure_tenent', ingestion_auth_tenent_type, options_list=['--tenent', '-t'])
        c.argument('configuration_file', configuration_file_type, options_list=['--configuration', '-f'])

    with self.argument_context('ingestion auth user') as c:
        c.argument('scope', ingestion_auth_scope_type, options_list=['--scope', '-sc'])

    with self.argument_context('ingestion auth platform') as c:
        c.argument('service_principal', ingestion_auth_type, options_list=['--service-principal', '-sp'])
        c.argument('dev_platform', ingestion_auth_type, options_list=['--dev-portal', '-dp'])
        c.argument('refresh_token', ingestion_auth_type, options_list=['--refresh-token', '-rt'])

    ##############################################
    # Platform Config
    ##############################################
    with self.argument_context('ingestion platform add', validator=configuration_file_validator) as c:
        c.argument('configuration_file', configuration_file_type, options_list=['--configuration', '-f'])

    with self.argument_context('ingestion platform show') as c:
        c.argument('platform_name', configuration_section_platform, options_list=['--name', '-n'])

    with self.argument_context('ingestion platform remove') as c:
        c.argument('platform_name', configuration_section_platform, options_list=['--name', '-n'])

    ##############################################
    # Tool Config
    ##############################################
    with self.argument_context('ingestion utility add', validator=configuration_file_validator) as c:
        c.argument('configuration_file', configuration_file_type, options_list=['--configuration', '-f'])

    with self.argument_context('ingestion utility show') as c:
        c.argument('utility_name', configuration_section_tool, options_list=['--name', '-n'])

    with self.argument_context('ingestion utility remove') as c:
        c.argument('utility_name', configuration_section_tool, options_list=['--name', '-n'])

    ##############################################
    # Tool Execute
    ##############################################
    with self.argument_context('ingestion execute', validator=configuration_file_validator) as c:
        c.argument('platform_name', configuration_section_platform, options_list=['--platform', '-p'])
        c.argument('utility_name', configuration_section_tool, options_list=['--utility', '-u'])
        c.argument('configuration_file', configuration_file_type, options_list=['--configuration', '-f'])
