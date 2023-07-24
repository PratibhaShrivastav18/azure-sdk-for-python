# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccountEncryption
from ._models_py3 import ActiveDirectory
from ._models_py3 import AuthorizeRequest
from ._models_py3 import Backup
from ._models_py3 import BackupPatch
from ._models_py3 import BackupPoliciesList
from ._models_py3 import BackupPolicy
from ._models_py3 import BackupPolicyPatch
from ._models_py3 import BackupRestoreFiles
from ._models_py3 import BackupStatus
from ._models_py3 import BackupsList
from ._models_py3 import BreakFileLocksRequest
from ._models_py3 import BreakReplicationRequest
from ._models_py3 import CapacityPool
from ._models_py3 import CapacityPoolList
from ._models_py3 import CapacityPoolPatch
from ._models_py3 import CheckAvailabilityResponse
from ._models_py3 import CloudErrorBody
from ._models_py3 import DailySchedule
from ._models_py3 import Dimension
from ._models_py3 import EncryptionIdentity
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ExportPolicyRule
from ._models_py3 import FilePathAvailabilityRequest
from ._models_py3 import GetGroupIdListForLDAPUserRequest
from ._models_py3 import GetGroupIdListForLDAPUserResponse
from ._models_py3 import HourlySchedule
from ._models_py3 import KeyVaultProperties
from ._models_py3 import LdapSearchScopeOpt
from ._models_py3 import ListReplications
from ._models_py3 import LogSpecification
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import MetricSpecification
from ._models_py3 import MonthlySchedule
from ._models_py3 import MountTarget
from ._models_py3 import MountTargetProperties
from ._models_py3 import NetAppAccount
from ._models_py3 import NetAppAccountList
from ._models_py3 import NetAppAccountPatch
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import PlacementKeyValuePairs
from ._models_py3 import PoolChangeRequest
from ._models_py3 import ProxyResource
from ._models_py3 import QuotaAvailabilityRequest
from ._models_py3 import ReestablishReplicationRequest
from ._models_py3 import RegionInfo
from ._models_py3 import RegionInfoAvailabilityZoneMappingsItem
from ._models_py3 import RelocateVolumeRequest
from ._models_py3 import Replication
from ._models_py3 import ReplicationObject
from ._models_py3 import ReplicationStatus
from ._models_py3 import Resource
from ._models_py3 import ResourceIdentity
from ._models_py3 import ResourceNameAvailabilityRequest
from ._models_py3 import RestoreStatus
from ._models_py3 import ServiceSpecification
from ._models_py3 import Snapshot
from ._models_py3 import SnapshotPoliciesList
from ._models_py3 import SnapshotPolicy
from ._models_py3 import SnapshotPolicyDetails
from ._models_py3 import SnapshotPolicyPatch
from ._models_py3 import SnapshotPolicyVolumeList
from ._models_py3 import SnapshotRestoreFiles
from ._models_py3 import SnapshotsList
from ._models_py3 import SubscriptionQuotaItem
from ._models_py3 import SubscriptionQuotaItemList
from ._models_py3 import SubvolumeInfo
from ._models_py3 import SubvolumeModel
from ._models_py3 import SubvolumePatchRequest
from ._models_py3 import SubvolumesList
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import Volume
from ._models_py3 import VolumeBackupProperties
from ._models_py3 import VolumeBackups
from ._models_py3 import VolumeGroup
from ._models_py3 import VolumeGroupDetails
from ._models_py3 import VolumeGroupList
from ._models_py3 import VolumeGroupMetaData
from ._models_py3 import VolumeGroupVolumeProperties
from ._models_py3 import VolumeList
from ._models_py3 import VolumePatch
from ._models_py3 import VolumePatchPropertiesDataProtection
from ._models_py3 import VolumePatchPropertiesExportPolicy
from ._models_py3 import VolumePropertiesDataProtection
from ._models_py3 import VolumePropertiesExportPolicy
from ._models_py3 import VolumeQuotaRule
from ._models_py3 import VolumeQuotaRulePatch
from ._models_py3 import VolumeQuotaRulesList
from ._models_py3 import VolumeRelocationProperties
from ._models_py3 import VolumeRevert
from ._models_py3 import VolumeSnapshotProperties
from ._models_py3 import WeeklySchedule

from ._net_app_management_client_enums import ActiveDirectoryStatus
from ._net_app_management_client_enums import ApplicationType
from ._net_app_management_client_enums import AvsDataStore
from ._net_app_management_client_enums import BackupType
from ._net_app_management_client_enums import CheckNameResourceTypes
from ._net_app_management_client_enums import CheckQuotaNameResourceTypes
from ._net_app_management_client_enums import ChownMode
from ._net_app_management_client_enums import CreatedByType
from ._net_app_management_client_enums import EnableSubvolumes
from ._net_app_management_client_enums import EncryptionKeySource
from ._net_app_management_client_enums import EncryptionType
from ._net_app_management_client_enums import EndpointType
from ._net_app_management_client_enums import FileAccessLogs
from ._net_app_management_client_enums import InAvailabilityReasonType
from ._net_app_management_client_enums import KeySource
from ._net_app_management_client_enums import KeyVaultStatus
from ._net_app_management_client_enums import ManagedServiceIdentityType
from ._net_app_management_client_enums import MetricAggregationType
from ._net_app_management_client_enums import MirrorState
from ._net_app_management_client_enums import NetworkFeatures
from ._net_app_management_client_enums import ProvisioningState
from ._net_app_management_client_enums import QosType
from ._net_app_management_client_enums import RegionStorageToNetworkProximity
from ._net_app_management_client_enums import RelationshipStatus
from ._net_app_management_client_enums import ReplicationSchedule
from ._net_app_management_client_enums import SecurityStyle
from ._net_app_management_client_enums import ServiceLevel
from ._net_app_management_client_enums import SmbAccessBasedEnumeration
from ._net_app_management_client_enums import SmbNonBrowsable
from ._net_app_management_client_enums import Type
from ._net_app_management_client_enums import VolumeStorageToNetworkProximity
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccountEncryption",
    "ActiveDirectory",
    "AuthorizeRequest",
    "Backup",
    "BackupPatch",
    "BackupPoliciesList",
    "BackupPolicy",
    "BackupPolicyPatch",
    "BackupRestoreFiles",
    "BackupStatus",
    "BackupsList",
    "BreakFileLocksRequest",
    "BreakReplicationRequest",
    "CapacityPool",
    "CapacityPoolList",
    "CapacityPoolPatch",
    "CheckAvailabilityResponse",
    "CloudErrorBody",
    "DailySchedule",
    "Dimension",
    "EncryptionIdentity",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExportPolicyRule",
    "FilePathAvailabilityRequest",
    "GetGroupIdListForLDAPUserRequest",
    "GetGroupIdListForLDAPUserResponse",
    "HourlySchedule",
    "KeyVaultProperties",
    "LdapSearchScopeOpt",
    "ListReplications",
    "LogSpecification",
    "ManagedServiceIdentity",
    "MetricSpecification",
    "MonthlySchedule",
    "MountTarget",
    "MountTargetProperties",
    "NetAppAccount",
    "NetAppAccountList",
    "NetAppAccountPatch",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PlacementKeyValuePairs",
    "PoolChangeRequest",
    "ProxyResource",
    "QuotaAvailabilityRequest",
    "ReestablishReplicationRequest",
    "RegionInfo",
    "RegionInfoAvailabilityZoneMappingsItem",
    "RelocateVolumeRequest",
    "Replication",
    "ReplicationObject",
    "ReplicationStatus",
    "Resource",
    "ResourceIdentity",
    "ResourceNameAvailabilityRequest",
    "RestoreStatus",
    "ServiceSpecification",
    "Snapshot",
    "SnapshotPoliciesList",
    "SnapshotPolicy",
    "SnapshotPolicyDetails",
    "SnapshotPolicyPatch",
    "SnapshotPolicyVolumeList",
    "SnapshotRestoreFiles",
    "SnapshotsList",
    "SubscriptionQuotaItem",
    "SubscriptionQuotaItemList",
    "SubvolumeInfo",
    "SubvolumeModel",
    "SubvolumePatchRequest",
    "SubvolumesList",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "Volume",
    "VolumeBackupProperties",
    "VolumeBackups",
    "VolumeGroup",
    "VolumeGroupDetails",
    "VolumeGroupList",
    "VolumeGroupMetaData",
    "VolumeGroupVolumeProperties",
    "VolumeList",
    "VolumePatch",
    "VolumePatchPropertiesDataProtection",
    "VolumePatchPropertiesExportPolicy",
    "VolumePropertiesDataProtection",
    "VolumePropertiesExportPolicy",
    "VolumeQuotaRule",
    "VolumeQuotaRulePatch",
    "VolumeQuotaRulesList",
    "VolumeRelocationProperties",
    "VolumeRevert",
    "VolumeSnapshotProperties",
    "WeeklySchedule",
    "ActiveDirectoryStatus",
    "ApplicationType",
    "AvsDataStore",
    "BackupType",
    "CheckNameResourceTypes",
    "CheckQuotaNameResourceTypes",
    "ChownMode",
    "CreatedByType",
    "EnableSubvolumes",
    "EncryptionKeySource",
    "EncryptionType",
    "EndpointType",
    "FileAccessLogs",
    "InAvailabilityReasonType",
    "KeySource",
    "KeyVaultStatus",
    "ManagedServiceIdentityType",
    "MetricAggregationType",
    "MirrorState",
    "NetworkFeatures",
    "ProvisioningState",
    "QosType",
    "RegionStorageToNetworkProximity",
    "RelationshipStatus",
    "ReplicationSchedule",
    "SecurityStyle",
    "ServiceLevel",
    "SmbAccessBasedEnumeration",
    "SmbNonBrowsable",
    "Type",
    "VolumeStorageToNetworkProximity",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
