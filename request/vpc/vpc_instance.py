# encoding: utf-8

import json
import time
from request.base_request import BaseRequest
from aliyunsdkvpc.request.v20160428.CreateVpcRequest import *
from aliyunsdkvpc.request.v20160428.DescribeVpcsRequest import *
from aliyunsdkvpc.request.v20160428.ModifyVpcAttributeRequest import *
from aliyunsdkvpc.request.v20160428.DeleteVpcRequest import *
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.acs_exception.exceptions import ClientException


class VPCInstance(BaseRequest):

    def create_vpc_instance(self, vpc_name, description, cidr_block):
        request = CreateVpcRequest()
        request.set_VpcName(vpc_name)
        request.set_Description(description)
        request.set_CidrBlock(cidr_block)
        try:
            response = json.loads(self.client.do_action_with_exception(request).decode('utf-8'))
        except (ServerException, ClientException)as e:
            print (e)
        else:
            print ("Create VPC instance with requestId : " + response.get("RequestId"))
            print ("The new created VPC with id : " + response.get("VpcId"))
            return response.get("VpcId")

    def create_vpc_instance_check_status(self, vpc_name, description, cidr_block):
        request = CreateVpcRequest()
        request.set_VpcName(vpc_name)
        request.set_Description(description)
        request.set_CidrBlock(cidr_block)
        try:
            response = json.loads(self.client.do_action_with_exception(request).decode('utf-8'))
        except (ServerException, ClientException)as e:
            print (e)
        else:
            print ("Create VPC instance with requestId : " + response.get("RequestId")+"")
            print ("The new created VPC with id : " + response.get("VpcId")+"")
            # Need to wait until the status for VPC instance is changed to Available
            target_id = response.get("VpcId")
            for i in range(0, self.max_retry_counts):
                vpc_status = self.describe_vpc_instance(target_id).get("Status")
                if vpc_status == self.target_status:
                    break
                else:
                    time.sleep(1)
            return target_id

    def describe_vpc_instance(self, vpc_id):
        request = DescribeVpcsRequest()
        request.set_VpcId(vpc_id)
        try:
            response = json.loads(self.client.do_action_with_exception(request).decode('utf-8'))
        except (ServerException, ClientException) as e:
            print (e)
        else:
            print ("Describe VPC instance with requestId : " + response.get("RequestId")+"")
            return response.get("Vpcs").get("Vpc")[0]

    def check_vpc_instance(self, vpc_id=None, vpc_name=None):
        request = DescribeVpcsRequest()
        if vpc_id is not None:
            request.set_VpcId(vpc_id)
        try:
            response = json.loads(self.client.do_action_with_exception(request).decode('utf-8'))
        except (ServerException, ClientException) as e:
            print(e)
        else:
            print("Describe VPC instance with requestId : " + response.get("RequestId") + "")
            results = response.get("Vpcs").get("Vpc")
            if len(results) == 0:
                # Check results list, if none VPC instance there, return None as vpc_id
                return None
            elif vpc_id is not None:
                # If check VPC instance with vpc_id, the list should contains one or empty
                return results[0].get("VpcId")
            elif vpc_name is not None:
                # If check VPC instance with vpc_name, should check every instance there
                for i in range(0, len(results)):
                    # Use contain instead of equal, caused by update function
                    # The test instance name may be test_python_instance or update_test_python_instance
                    if vpc_name in results[i].get("VpcName"):
                        return results[i].get("VpcId")
                return None
            else:
                # Return None directly if both vpc_id and vpc_name are None
                return None

    def modify_vpc_instance(self, vpc_id, description, vpc_name):
        request = ModifyVpcAttributeRequest()
        request.set_VpcId(vpc_id)
        request.set_Description(description)
        request.set_VpcName(vpc_name)
        try:
            response = json.loads(self.client.do_action_with_exception(request).decode('utf-8'))
        except (ServerException, ClientException) as e:
            print(e)
        else:
            print ("Modify VPC instance with requestId : " + response.get("RequestId")+"")
            return response

    def delete_vpc_instance(self, vpc_id):
        request = DeleteVpcRequest()
        request.set_VpcId(vpc_id)
        try:
            response = json.loads(self.client.do_action_with_exception(request).decode('utf-8'))
        except (ServerException, ClientException) as e:
            print(e)
        else:
            print ("Delete VPC instance with requestId : " + response.get("RequestId")+"")
            return response
