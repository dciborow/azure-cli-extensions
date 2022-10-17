# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests
from knack.util import CLIError
from azure.cli.core.auth.msal_authentication import UserCredential
from azure.cli.core import AzCli
from .contracts.IDDCProvider import IDDCProvider

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

class DDCProvider(IDDCProvider):

    def __init__(self, user_info:CliUserInfo):
        self.user_info = user_info

    def create(self) -> dict:
        raise CLIError('TODO: Implement `gaming create`')

    def list(self) -> dict:
        raise CLIError('TODO: Implement `gaming list`')
