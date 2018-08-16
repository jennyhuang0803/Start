# encoding: utf-8

from request.log.log_project import LOGProject
from behave import given, when, then
from hamcrest import *

DEFAULT_PROJECT_NAME = "python-test-sdk"
DEFAULT_PROJECT_STATUS = "Normal"
log_project = LOGProject()


@when("I create a log project")
def create_log_project(context):
    context.log_description = "This is used to test python sdk for log"
    log_project.create_project(DEFAULT_PROJECT_NAME, context.log_description)


@then("I could see the new created log project")
def check_created_log_project(context):
    project = log_project.get_project(DEFAULT_PROJECT_NAME)
    print ("Check project name with : " + project.projectName)
    assert_that(DEFAULT_PROJECT_NAME, equal_to(project.projectName))
    print ("Check project description with : " + project.description)
    assert_that(context.log_description, equal_to(project.description))
    print ("Check project status with : " + project.status)
    assert_that(DEFAULT_PROJECT_STATUS, equal_to(project.status))


@given("I have a log project")
def check_existing_log_project(context):
    result = log_project.check_existing_project(DEFAULT_PROJECT_NAME, DEFAULT_PROJECT_STATUS)
    if result:
        print ("Target log project exists, no need to create again.")
    else:
        create_log_project(context)


@when("I delete the log project")
def delete_log_project(context):
    log_project.delete_project(DEFAULT_PROJECT_NAME)


@then("I could not see the log project")
def check_deleted_log_project(context):
    result = log_project.check_existing_project(DEFAULT_PROJECT_NAME, DEFAULT_PROJECT_STATUS)
    assert_that(result, is_(False))
