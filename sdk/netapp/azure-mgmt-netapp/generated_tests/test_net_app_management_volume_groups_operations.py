# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.netapp import NetAppManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetAppManagementVolumeGroupsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetAppManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_net_app_account(self, resource_group):
        response = self.client.volume_groups.list_by_net_app_account(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-03-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.volume_groups.get(
            resource_group_name=resource_group.name,
            account_name="str",
            volume_group_name="str",
            api_version="2024-03-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create(self, resource_group):
        response = self.client.volume_groups.begin_create(
            resource_group_name=resource_group.name,
            account_name="str",
            volume_group_name="str",
            body={
                "groupMetaData": {
                    "applicationIdentifier": "str",
                    "applicationType": "str",
                    "globalPlacementRules": [{"key": "str", "value": "str"}],
                    "groupDescription": "str",
                    "volumesCount": 0,
                },
                "id": "str",
                "location": "str",
                "name": "str",
                "provisioningState": "str",
                "type": "str",
                "volumes": [
                    {
                        "creationToken": "str",
                        "subnetId": "str",
                        "usageThreshold": 107374182400,
                        "actualThroughputMibps": 0.0,
                        "avsDataStore": "Disabled",
                        "backupId": "str",
                        "baremetalTenantId": "str",
                        "capacityPoolResourceId": "str",
                        "cloneProgress": 0,
                        "coolAccess": False,
                        "coolAccessRetrievalPolicy": "str",
                        "coolnessPeriod": 0,
                        "dataProtection": {
                            "backup": {"backupPolicyId": "str", "backupVaultId": "str", "policyEnforced": bool},
                            "replication": {
                                "remoteVolumeResourceId": "str",
                                "endpointType": "str",
                                "remoteVolumeRegion": "str",
                                "replicationId": "str",
                                "replicationSchedule": "str",
                            },
                            "snapshot": {"snapshotPolicyId": "str"},
                            "volumeRelocation": {"readyToBeFinalized": bool, "relocationRequested": bool},
                        },
                        "dataStoreResourceId": ["str"],
                        "defaultGroupQuotaInKiBs": 0,
                        "defaultUserQuotaInKiBs": 0,
                        "deleteBaseSnapshot": bool,
                        "enableSubvolumes": "Disabled",
                        "encrypted": bool,
                        "encryptionKeySource": "Microsoft.NetApp",
                        "exportPolicy": {
                            "rules": [
                                {
                                    "allowedClients": "str",
                                    "chownMode": "Restricted",
                                    "cifs": bool,
                                    "hasRootAccess": True,
                                    "kerberos5ReadOnly": False,
                                    "kerberos5ReadWrite": False,
                                    "kerberos5iReadOnly": False,
                                    "kerberos5iReadWrite": False,
                                    "kerberos5pReadOnly": False,
                                    "kerberos5pReadWrite": False,
                                    "nfsv3": bool,
                                    "nfsv41": bool,
                                    "ruleIndex": 0,
                                    "unixReadOnly": bool,
                                    "unixReadWrite": bool,
                                }
                            ]
                        },
                        "fileAccessLogs": "Disabled",
                        "fileSystemId": "str",
                        "id": "str",
                        "isDefaultQuotaEnabled": False,
                        "isLargeVolume": False,
                        "isRestoring": bool,
                        "kerberosEnabled": False,
                        "keyVaultPrivateEndpointResourceId": "str",
                        "ldapEnabled": False,
                        "maximumNumberOfFiles": 0,
                        "mountTargets": [
                            {"fileSystemId": "str", "ipAddress": "str", "mountTargetId": "str", "smbServerFqdn": "str"}
                        ],
                        "name": "str",
                        "networkFeatures": "Basic",
                        "networkSiblingSetId": "str",
                        "originatingResourceId": "str",
                        "placementRules": [{"key": "str", "value": "str"}],
                        "protocolTypes": ["str"],
                        "provisionedAvailabilityZone": "str",
                        "provisioningState": "str",
                        "proximityPlacementGroup": "str",
                        "securityStyle": "unix",
                        "serviceLevel": "Premium",
                        "smbAccessBasedEnumeration": "str",
                        "smbContinuouslyAvailable": False,
                        "smbEncryption": False,
                        "smbNonBrowsable": "str",
                        "snapshotDirectoryVisible": True,
                        "snapshotId": "str",
                        "storageToNetworkProximity": "str",
                        "t2Network": "str",
                        "tags": {"str": "str"},
                        "throughputMibps": 0.0,
                        "type": "str",
                        "unixPermissions": "str",
                        "volumeGroupName": "str",
                        "volumeSpecName": "str",
                        "volumeType": "str",
                        "zones": ["str"],
                    }
                ],
            },
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.volume_groups.begin_delete(
            resource_group_name=resource_group.name,
            account_name="str",
            volume_group_name="str",
            api_version="2024-03-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
