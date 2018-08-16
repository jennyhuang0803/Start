# encoding: utf-8

from request.vpc.vpc_instance import VPCInstance
from behave import given, when, then
from hamcrest import *

DEFAULT_VPC_INSTANCE_NAME = "test_python_instance"
vpc_instance_request = VPCInstance()


@given("I have a VPC instance")
def check_existing_vpc_instance(context):
    target_id = vpc_instance_request.check_vpc_instance(vpc_name=DEFAULT_VPC_INSTANCE_NAME)
    if target_id is not None:
        print("Already have VPC instance with Name : " + DEFAULT_VPC_INSTANCE_NAME + " and id : " + target_id)
        context.vpc_id = target_id
    else:
        print ("Do not have VPC instance with name " + DEFAULT_VPC_INSTANCE_NAME + " and need to create it")
        create_vpc_instance(context)


@when("I create a VPC instance")
def create_vpc_instance(context):
    context.vpc_description = "This is used to test python sdk for vpc"
    context.vpc_cidr_block = "10.0.0.0/8"
    vpc_id = vpc_instance_request.create_vpc_instance_check_status(DEFAULT_VPC_INSTANCE_NAME, context.vpc_description,
                                                                     context.vpc_cidr_block)
    context.vpc_id = vpc_id


@then("I can see the new created instance")
def check_created_vpc_instance(context):
    assert_that(context.vpc_id, not_none())
    vpc_info = vpc_instance_request.describe_vpc_instance(context.vpc_id)
    print ("Checking VPC instance Id : " + vpc_info.get("VpcId"))
    assert_that(context.vpc_id, equal_to(vpc_info.get("VpcId")))
    print ("Checking VPC instance name : " + vpc_info.get("VpcName"))
    assert_that(DEFAULT_VPC_INSTANCE_NAME, equal_to(vpc_info.get("VpcName")))
    print ("Checking VPC instance description : " + vpc_info.get("Description"))
    assert_that(context.vpc_description, equal_to(vpc_info.get("Description")))
    print ("Checking VPC instance cidrblock : " + vpc_info.get("CidrBlock"))
    assert_that(context.vpc_cidr_block, equal_to(vpc_info.get("CidrBlock")))


@when("I update the attributes of the VPC instance")
def update_vpc_instance(context):
    context.vpc_name_update = "update_test_python_instance"
    context.vpc_description_update = "Update This is used to test python sdk for vpc"
    vpc_instance_request.modify_vpc_instance(context.vpc_id, context.vpc_description_update, context.vpc_name_update)


@then("I can see the updated attributes")
def check_updated_vpc_instance(context):
    assert_that(context.vpc_id, not_none())
    vpc_info = vpc_instance_request.describe_vpc_instance(context.vpc_id)
    print ("Checking VPC instance Id : " + vpc_info.get("VpcId"))
    assert_that(context.vpc_id, equal_to(vpc_info.get("VpcId")))
    print ("Checking VPC instance name : " + vpc_info.get("VpcName"))
    assert_that(context.vpc_name_update, equal_to(vpc_info.get("VpcName")))
    print ("Checking VPC instance description : " + vpc_info.get("Description"))
    assert_that(context.vpc_description_update, equal_to(vpc_info.get("Description")))


@when("I delete the VPC instance")
def delete_vpc_instance(context):
    vpc_instance_request.delete_vpc_instance(context.vpc_id)


@then("I can not see the instance")
def check_deleted_vpc_instance(context):
    target_id = vpc_instance_request.check_vpc_instance(vpc_id=context.vpc_id)
    assert_that(target_id, none())
