# encoding: utf-8

from common.client_factory import ClientFactory


class BaseLogRequest:
    __instance = None
    client = ClientFactory(client_type="log").get_log_client()
    max_retry_counts = 5
    target_status = "Normal"

    def __init__(self):
        pass

    def __new__(cls, *args, **kwd):
        if BaseLogRequest.__instance is None:
            BaseLogRequest.__instance = object.__new__(cls, *args, **kwd)
        return BaseLogRequest.__instance