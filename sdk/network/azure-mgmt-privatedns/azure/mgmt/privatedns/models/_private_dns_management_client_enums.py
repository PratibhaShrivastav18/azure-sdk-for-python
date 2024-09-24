# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the resource. This is a read-only property and any attempt to set
    this value will be ignored.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class RecordType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RecordType."""

    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"
    MX = "MX"
    PTR = "PTR"
    SOA = "SOA"
    SRV = "SRV"
    TXT = "TXT"


class ResolutionPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The resolution policy on the virtual network link. Only applicable for virtual network links to
    privatelink zones, and for A,AAAA,CNAME queries. When set to 'NxDomainRedirect', Azure DNS
    resolver falls back to public resolution if private dns query resolution results in
    non-existent domain response.
    """

    DEFAULT = "Default"
    NX_DOMAIN_REDIRECT = "NxDomainRedirect"


class VirtualNetworkLinkState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the virtual network link to the Private DNS zone. Possible values are
    'InProgress' and 'Done'. This is a read-only property and any attempt to set this value will be
    ignored.
    """

    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
