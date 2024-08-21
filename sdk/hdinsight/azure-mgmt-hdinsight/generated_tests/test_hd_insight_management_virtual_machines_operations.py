# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.hdinsight import HDInsightManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestHDInsightManagementVirtualMachinesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(HDInsightManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_hosts(self, resource_group):
        response = self.client.virtual_machines.list_hosts(
            resource_group_name=resource_group.name,
            cluster_name="str",
            api_version="2024-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_restart_hosts(self, resource_group):
        response = self.client.virtual_machines.begin_restart_hosts(
            resource_group_name=resource_group.name,
            cluster_name="str",
            hosts=["str"],
            api_version="2024-08-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get_async_operation_status(self, resource_group):
        response = self.client.virtual_machines.get_async_operation_status(
            resource_group_name=resource_group.name,
            cluster_name="str",
            operation_id="str",
            api_version="2024-08-01-preview",
        )

        # please add some check logic here by yourself
        # ...
