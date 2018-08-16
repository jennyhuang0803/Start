# encoding: utf-8

from request.base_log_request import BaseLogRequest


class LogStore(BaseLogRequest):

    def create_log_logstore(self):
        self.client.create_project()
