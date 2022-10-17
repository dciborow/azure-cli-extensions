# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_gaming.manual.src.contracts.IResourceProvider import IResourceProvider

""" Original template unused
def create_gaming(cmd, client, resource_group_name, gaming_name, location=None, tags=None):
    raise CLIError('TODO: Implement `gaming create`')


def list_gaming(cmd, client, resource_group_name=None):
    raise CLIError('TODO: Implement `gaming list`')

def update_gaming(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance
"""

############################################
# Unreal Cloud DDC
############################################
def create_gdvm(cmd, client: IResourceProvider, resource_group_name, name, location=None, tags=None):
    return client.create(location=location, resource_group_name=resource_group_name, name=name)


def list_gdvm(cmd, client: IResourceProvider, resource_group_name, location=None):
    return client.list(location=location, resource_group_name=resource_group_name)


def create_ddc(cmd, client: IResourceProvider, resource_group_name, name, location=None, tags=None):
    return client.create()


def list_ddc(cmd, client: IResourceProvider, resource_group_name=None):
    return client.list()


def create_pixel_streaming(cmd, client: IResourceProvider, resource_group_name, name, location=None, tags=None):
    return client.create()


def list_pixel_streaming(cmd, client: IResourceProvider, resource_group_name=None):
    return client.list()
