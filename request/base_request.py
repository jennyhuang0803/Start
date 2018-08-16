# encoding: utf-8

from common.client_factory import ClientFactory


class BaseRequest:
    __instance = None
    # This is for new session ak
    # client = ClientFactory(client_type="new_ak").get_acs_client()
    # This is for access key
    client = ClientFactory().get_acs_client()
    max_retry_counts = 5
    target_status = "Available"

    def __init__(self):
        pass

    def __new__(cls, *args, **kwd):
        if BaseRequest.__instance is None:
            BaseRequest.__instance = object.__new__(cls, *args, **kwd)
        return BaseRequest.__instance
