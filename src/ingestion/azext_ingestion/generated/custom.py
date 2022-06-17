# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
import requests

def create_ingestion(cmd, client, resource_group_name, ingestion_name, location=None, tags=None):
    raise CLIError('TODO: Implement `ingestion create`')


def list_ingestion(cmd, client, resource_group_name=None):
    raise CLIError('TODO: Implement `ingestion list` darn it')

def update_ingestion(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance

# Functionality implemented. 
def get_token(cmd, client, azure_tenent, service_principal, service_principal_secret, configuration_file):
    client.prepare(azure_tenent, service_principal, service_principal_secret, configuration_file)
    return client.acquire_token()
