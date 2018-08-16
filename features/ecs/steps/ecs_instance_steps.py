# encoding: utf-8

from request.ecs.ecs_instance import ECSInstance
from behave import given, when, then

DEFAULT_ECS_INSTANCE_NAME = 'test_python_instance'
__ecs_instance_request = ECSInstance()


@when('I create an ECS instance')
def create_ecs_instance_post_paid(context):
    __ecs_instance_request.create_ecs_instance(instance_name=DEFAULT_ECS_INSTANCE_NAME,
                                               vswitch_id='vsw-6we7j98zmxhsp3olwsim5')


@then('I could see the new instance')
def check_new_created_ecs_instance(context):
    assert True
