# encoding: utf-8

from steps import vpc_instance_steps


def after_tag(context, tag):
    if tag == "vpc_instance_release":
        if context.vpc_id is not None:
            target_id = context.vpc_id
        else:
            target_id = vpc_instance_steps.vpc_instance_request.check_vpc_instance(
                vpc_name=vpc_instance_steps.DEFAULT_VPC_INSTANCE_NAME)
        if target_id is not None:
            print ("Need clear existing vpc instance with id : " + target_id)
            vpc_instance_steps.vpc_instance_request.delete_vpc_instance(target_id)
        else:
            print ("No existing test resource there")
