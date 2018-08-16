# encoding: utf-8

from aliyunsdkecs.request.v20140526.CreateInstanceRequest import *
from common.client_factory import ClientFactory
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.acs_exception.exceptions import ClientException


class ECSInstance:
    def __init__(self):
        self.__client = ClientFactory().get_acs_client()

    def create_ecs_instance(self, image_id='ubuntu_16_0402_64_20G_alibase_20170818.vhd', instance_type='ecs.xn4.small',
                            instance_charge_type='PostPaid', instance_name=None, vswitch_id=None, accept_format='json',
                            description=None):
        request = CreateInstanceRequest()
        # required field
        request.set_ImageId(image_id)
        request.set_InstanceType(instance_type)
        request.set_InstanceChargeType(instance_charge_type)
        request.set_InstanceName(instance_name)
        request.set_VSwitchId(vswitch_id)
        request.set_accept_format(accept_format)
        # not mandatory
        request.set_Description(description)
        # .......
        try:
            response = self.__client.do_action_with_exception(request)
        except (ServerException, ClientException), e:
            print e
        else:
            print response
            return response
