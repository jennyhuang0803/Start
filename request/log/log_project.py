# encoding: utf-8

import time

from aliyun.log.logexception import LogException

from request.base_log_request import BaseLogRequest


class LOGProject(BaseLogRequest):
    def create_project(self, project_name, project_des):
        try:
            response = self.client.create_project(project_name, project_des)
        except LogException as e:
            print("LogException : ", e)
        else:
            response.log_print()
            # Wait until create action finished, need enhancement later
            time.sleep(30)

    def get_project(self, project_name):
        try:
            response = self.client.get_project(project_name)
        except LogException as e:
            print("LogException : ", e)
        else:
            return response

    def delete_project(self, project_name):
        try:
            response = self.client.delete_project(project_name)
        except LogException as e:
            print("LogException : ", e)
        else:
            response.log_print()
            # Wait until delete action finished, need enhancement later
            time.sleep(30)

    def check_existing_project(self, project_name, project_status):
        try:
            results = self.client.list_project().projects
        except LogException as e:
            print("LogException : ", e)
        else:
            flag = False
            if len(results) == 0:
                return flag
            else:
                for i in range(0, len(results)):
                    if project_name == results[i]["projectName"] and project_status == results[i]["status"]:
                        print("Find existing project with name : " + project_name + " and status : " + project_status)
                        flag = True
                        return flag
                return flag
