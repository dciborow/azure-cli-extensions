# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests
from knack.util import CLIError
from azure.cli.core.auth.msal_authentication import UserCredential
from azure.cli.core import AzCli
from .contracts.IUserTokenProvider import IUserTokenProvider

class CliUserInfo:
    def __init__(self,cli_ctx:AzCli):
        from azure.cli.core._profile import Profile
        
        profile = Profile(cli_ctx=cli_ctx)
        cred, subscription_id, tenant = profile.get_login_credentials()
        management_token = cred._credential.get_token("https://management.azure.com/.default")

        self.subscription_id = subscription_id 
        self.user_tenent:str = tenant
        self.user_cred:UserCredential = cred._credential
        self.user_account:dict = cred._credential._account
        self.user_mgmt_token:str = management_token.token

    def get_token(self, scope:str):
        return self.user_cred.get_token(scope).token

class UserTokenProvider(IUserTokenProvider):

    def __init__(self, user_info:CliUserInfo):
        self.user_info = user_info

    def acquire_token(self, scope:str) -> dict:
        return { "token" : self.user_info.get_token(scope)}

    def acquire_platform_token(self, refresh_token:str, client_id:str, dev_portal:str) -> dict:
        login_base = "login.microsoftonline.com/{}".format(self.user_info.user_tenent)
        oauth_token_host = "{}/oauth2/v2.0/token".format(login_base)
        token_url = "https://{}".format(oauth_token_host)
        scopes = "{}/.default openid profile offline_access".format(client_id)

        headers = {}
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Origin"] = dev_portal

        request_body = """
            grant_type=refresh_token
            &client_id={CLIENT_ID}
            &refresh_token={REFRESH_TOKEN}
            &scope={SCOPES}
            """.format(CLIENT_ID=client_id, REFRESH_TOKEN=refresh_token, SCOPES=scopes )

        response = requests.post(url=token_url, headers=headers, data=request_body)

        if response.status_code == 200:
            response_json = response.json()
            return {"token" : response_json["access_token"]} 
        else:
            raise CLIError('Error retrieving token: {}\n{}'.format(response.status_code, response.text))
