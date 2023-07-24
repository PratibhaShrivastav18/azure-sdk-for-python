# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.netapp import NetAppManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-netapp
# USAGE
    python snapshot_policies_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetAppManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="D633CC2E-722B-4AE1-B636-BBD9E4C60ED9",
    )

    response = client.snapshot_policies.begin_update(
        resource_group_name="myRG",
        account_name="account1",
        snapshot_policy_name="snapshotPolicyName",
        body={
            "location": "eastus",
            "properties": {
                "dailySchedule": {"hour": 14, "minute": 30, "snapshotsToKeep": 4},
                "enabled": True,
                "hourlySchedule": {"minute": 50, "snapshotsToKeep": 2},
                "monthlySchedule": {"daysOfMonth": "10,11,12", "hour": 14, "minute": 15, "snapshotsToKeep": 5},
                "weeklySchedule": {"day": "Wednesday", "hour": 14, "minute": 45, "snapshotsToKeep": 3},
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/netapp/resource-manager/Microsoft.NetApp/stable/2022-11-01/examples/SnapshotPolicies_Update.json
if __name__ == "__main__":
    main()
