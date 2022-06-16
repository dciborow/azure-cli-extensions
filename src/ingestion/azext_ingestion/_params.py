# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    ingestion_name_type = CLIArgumentType(options_list='--ingestion-name-name', help='Name of the Ingestion.', id_part='name')
    ingestion_auth_type = CLIArgumentType(options_list='--ingestion-auth-sp', help='Service Principal ID.', id_part='sp')
    ingestion_auth_secret_type = CLIArgumentType(options_list='--ingestion-auth-secret', help='Service Principal Secret.', id_part='secret')
    ingestion_auth_tenent_type = CLIArgumentType(options_list='--ingestion-auth-tenent', help='Active Directory Tenent', id_part='tenent')

    with self.argument_context('ingestion') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('ingestion_name', ingestion_name_type, options_list=['--name', '-n'])
        c.argument('service_principal', ingestion_auth_type, options_list=['--service-principal', '-p'])
        c.argument('service_principal_secret', ingestion_auth_secret_type, options_list=['--service-principal-credential', '-c'])
        c.argument('azure_tenent', ingestion_auth_tenent_type, options_list=['--tenent', '-t'])

    with self.argument_context('ingestion list') as c:
        c.argument('ingestion_name', ingestion_name_type, id_part=None)
