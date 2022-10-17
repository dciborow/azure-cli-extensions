# azure-cli-extensions


Example dxtensions repository, see the other repo [azure-cli-extension](https://github.com/grecoe/azure-cli-extension) for more details on how this is used.


The example extension here extends the Azure CLI with the following command:

> az gaming ....

This batch of commands mimic the required settings manage a PaaS service and interact with it. 

Configuration information used by the extension is stored in the following location on the users disk. It is not stored in Azure, so context is lost between machines. 

> /platform_user_path/.azext_gaming

<b>Contents</b>
- [Command Flow](#token-flow)
- [Commands](#commands)


Might come in handy, [management client](https://github.com/Azure/azure-cli-extensions/blob/main/src/aks-preview/azext_aks_preview/_client_factory.py)

## Token Flow 
This flow is for grabbing a platform token. 

![flow](./images/flow.jpg)

## Commands

The commands here are to be filled out to cover a range of items, however they have not been fully defined yet. 

Actions such as create, list, show, delete of the platform are not incoroporated. Those, likely, will come from some generated code from an actual service in Azure. 

The commands here are generally pretty basic to 
- Generate authentication tokens
    - These are not fully complete, but it's unclear if they need to be. 
- Store settings for individual platforms or registered utility applications
    - This CLI instance may end up just being a wrapper over other local utilities written by open communities or others. 
- Job execution
    - This is in a rudimentary state, but flushed out enough to build a design from it. 

    

- az gaming 
```bash
Group
    az gaming : Commands to manage Gaming Platform.
Subgroups:
    auth
    execute
    platform
    utility
```

- az gaming auth
```bash
Group
    az gaming auth
Commands:
    platform : Get authentication token from existing platform refresh token.
    sp       : Get authentication token for service principal.
    user     : Get authentication token for current user.
```

- az gaming platform
```bash
Group
    az gaming platform
Commands:
    add    : Adds an OSDU platform configuration to cli settings.
    list
    remove
    show
```

- az gaming utility
```bash
Group
    az gaming utility
Commands:
    add    : Adds a utility configuration to the settings.
    list
    remove
    show
```

- az gaming execute
```bash
Group
    az gaming execute
Commands:
    job
```
