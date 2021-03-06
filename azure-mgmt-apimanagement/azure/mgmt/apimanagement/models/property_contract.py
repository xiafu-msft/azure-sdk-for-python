# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class PropertyContract(Resource):
    """Property details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param tags: Optional tags that when provided can be used to filter the
     property list.
    :type tags: list[str]
    :param secret: Determines whether the value is a secret and should be
     encrypted or not. Default value is false.
    :type secret: bool
    :param display_name: Required. Unique name of Property. It may contain
     only letters, digits, period, dash, and underscore characters.
    :type display_name: str
    :param value: Required. Value of the property. Can contain policy
     expressions. It may not be empty or consist only of whitespace.
    :type value: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'max_items': 32},
        'display_name': {'required': True, 'max_length': 256, 'min_length': 1, 'pattern': r'^[A-Za-z0-9-._]+$'},
        'value': {'required': True, 'max_length': 4096, 'min_length': 1},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'properties.tags', 'type': '[str]'},
        'secret': {'key': 'properties.secret', 'type': 'bool'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'value': {'key': 'properties.value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PropertyContract, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.secret = kwargs.get('secret', None)
        self.display_name = kwargs.get('display_name', None)
        self.value = kwargs.get('value', None)
