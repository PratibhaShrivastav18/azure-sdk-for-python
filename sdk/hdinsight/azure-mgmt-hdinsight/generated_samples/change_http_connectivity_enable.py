# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.hdinsight import HDInsightManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hdinsight
# USAGE
    python change_http_connectivity_enable.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HDInsightManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    client.configurations.begin_update(
        resource_group_name="rg1",
        cluster_name="cluster1",
        configuration_name="gateway",
        parameters={
            "restAuthCredential.isEnabled": "true",
            "restAuthCredential.password": "**********",
            "restAuthCredential.username": "hadoop",
        },
    ).result()


# x-ms-original-file: specification/hdinsight/resource-manager/Microsoft.HDInsight/preview/2024-08-01-preview/examples/ChangeHttpConnectivityEnable.json
if __name__ == "__main__":
    main()
