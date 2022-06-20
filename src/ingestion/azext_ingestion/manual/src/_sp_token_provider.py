# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests
from knack.util import CLIError
from .contracts.ITokenProvider import ITokenProvider

class SPTokenConfigurationService(ITokenProvider):
    """
    Service used to request an access token for a service principal. 
    """
    PRINCIPAL = "service_principal"
    CREDENTIAL =  "service_principal_secret" 
    TENENT = "azure_tenent"

    def __init__(self):
        self.tenent = None
        self.principal_id = None
        self.principal_cred = None
        self.configuration = None

    def prepare(self, tenent, principal, credential, configuration):
        if tenent and principal and credential:
            self.tenent = tenent
            self.principal_id = principal
            self.principal_cred = credential
        else:
            self.configuration = configuration

            content = None
            with open(configuration, "r") as config:
                content = config.readlines()
                content = "\n".join(content)
            
            try:
                import json
                content = json.loads(content)
            except Exception as ex:
                raise CLIError("{} is invalid JSON for configuration".format(configuration))

            if SPTokenConfigurationService.PRINCIPAL in content:
                self.principal_id = content[SPTokenConfigurationService.PRINCIPAL]
            else:
                raise CLIError("{} required in configuration file", SPTokenConfigurationService.PRINCIPAL)

            if SPTokenConfigurationService.CREDENTIAL in content:
                self.principal_cred = content[SPTokenConfigurationService.CREDENTIAL]
            else:
                raise CLIError("{} required in configuration file", SPTokenConfigurationService.CREDENTIAL)

            if SPTokenConfigurationService.TENENT in content:
                self.tenent = content[SPTokenConfigurationService.TENENT]
            else:
                raise CLIError("{} required in configuration file", SPTokenConfigurationService.TENENT)


    def acquire_token(self) -> dict:
        login_base = "login.microsoftonline.com/{}".format(self.tenent)
        oauth_token_host = "{}/oauth2/token".format(login_base) 
        token_url = "https://{}".format(oauth_token_host)

        headers = {}
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        request_body = """
            grant_type=client_credentials
            &client_id={CLIENT_ID}
            &client_secret={CLIENT_SECRET}
            &resource={CLIENT_ID}
            """.format(CLIENT_ID=self.principal_id, CLIENT_SECRET=self.principal_cred)

        response = requests.post(url=token_url, headers=headers, data=request_body)

        if response.status_code == 200:
            response_json = response.json()
            return {"token" : response_json["access_token"]} 
        else:
            raise CLIError('Error retrieving token: {}\n{}'.format(response.status_code, response.text))
