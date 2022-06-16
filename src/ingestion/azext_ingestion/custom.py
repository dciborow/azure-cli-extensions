# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
import requests

def create_ingestion(cmd, resource_group_name, ingestion_name, location=None, tags=None):
    raise CLIError('TODO: Implement `ingestion create`')


def list_ingestion(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `ingestion list` darn it')

def get_token(cmd, azure_tenent, service_principal, service_principal_secret):

    login_base = "login.microsoftonline.com/{}".format(azure_tenent)
    oauth_token_host = "{}/oauth2/token".format(login_base) 
    token_url = "https://{}".format(oauth_token_host)

    headers = {}
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    request_body = """
    grant_type=client_credentials
    &client_id={CLIENT_ID}
    &client_secret={CLIENT_SECRET}
    &resource={CLIENT_ID}
    """.format(CLIENT_ID=service_principal, CLIENT_SECRET=service_principal_secret)

    response = requests.post(url=token_url, headers=headers, data=request_body)

    if response.status_code == 200:
        response_json = response.json()

        print("Your access token is:")
        print(response_json["access_token"])
    else:
        raise CLIError('Error retrieving token: {}'.format(response.status_code))


def update_ingestion(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance