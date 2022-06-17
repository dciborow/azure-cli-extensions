# azure-cli-extensions


Example dxtensions repository, see the other repo [azure-cli-extension](https://github.com/grecoe/azure-cli-extension) for more details on how this is used.


The example extension here extends the Azure CLI with the following command:
> az ingestion ....

While there are a couple of actions this extension can take, the only one that does anything is the sub command group:
> az ingestion token get

What is used in this repo (code under src/ingestion/azext_ingestion)

|Location|File|Interest|
|---|----|----|
|.|__ init __.py|Prepares the commands to be called by the cli engine.|
|.|custom.py|Imports calls to expose under generated/|
|./generated|_params.py|Set up parameters and a parameter validation for the calls.|
|./generated|_validators.py|Implements the parameter validators used in _params.py|
|./generated|_help.py|The help shown when requested by the user.|
|./generated|_client_factory.py|Clients that can be dynamically passed to calls.|
|./generated|commands.py|Creates a sub group of calls|
|./generated|custom.py|Contains the actual action call to get a token.|


Might come in handy, [management client](https://github.com/Azure/azure-cli-extensions/blob/main/src/aks-preview/azext_aks_preview/_client_factory.py)