# encoding: utf-8


from aliyun.log.logclient import LogClient
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider

from common import config


class ClientFactory:
    def __init__(self, client_type="ak", access_key_id=None, access_secret=None, region_id=None, public_key_id=None,
                 private_key=None, session_period=3600, endpoint=None):
        """
        Client factory is used to generate related client
        Could get instance of AcsClient and other client such as OTSClient and so on in the future
        :param client_type: this is used to decide how to generate AcsClient, ak or new_ak
        :param access_key_id: account access key id, will get from conf file if None
        :param access_secret: account access secret, will get from conf file if None
        :param region_id: region id, will get from conf file if None
        :param public_key_id: public key id for new session ak
        :param private_key: private key for new session ak
        :param session_period: session period for new session ak
        :param endpoint: Used for generate log client
        """
        self.__access_key_id = access_key_id
        self.__access_secret = access_secret
        self.__region_id = region_id
        self.__public_key_id = public_key_id
        self.__private_key = private_key
        self.__session_period = session_period
        self.__endpoint = endpoint
        if client_type == "new_ak":
            self.__acs_client = self.__generate_acs_client_with_new_ak()
        elif client_type == "log":
            self.__log_client = self.__generate_log_client()
        else:
            self.__acs_client = self.__generate_acs_client()

    def get_acs_client(self):
        if self.__acs_client is None:
            self.__acs_client = self.__generate_acs_client()
        return self.__acs_client

    def get_log_client(self):
        if self.__log_client is None:
            self.__log_client = self.__generate_log_client()
        return self.__log_client

    def __generate_acs_client(self):
        if self.__access_key_id is None:
            self.__access_key_id = config.get_config('account_info', 'access_key_id')
        if self.__access_secret is None:
            self.__access_secret = config.get_config('account_info', 'access_secret')
        if self.__region_id is None:
            self.__region_id = config.get_config('region_info', 'region_id')
        print("Generate AcsClient with Access Key and Access Secret in Region : " + self.__region_id)
        self.__acs_client = AcsClient(self.__access_key_id, self.__access_secret, self.__region_id)
        return self.__acs_client

    def __generate_acs_client_with_new_ak(self):
        if self.__public_key_id is None:
            self.__public_key_id = config.get_config('new_ak', 'public_key_id')
        if self.__private_key is None:
            self.__private_key = config.get_config('new_ak', 'private_key')
        if self.__session_period is None:
            self.__session_period = config.get_config('new_ak', 'session_period')
        if self.__region_id is None:
            self.__region_id = config.get_config('region_info', 'region_id')
        print("Generate AcsClient with New Session AK in Region : " + self.__region_id)
        region_provider.modify_point('Sts', self.__region_id, 'sts.' + self.__region_id + '.aliyuncs.com')
        self.__acs_client = AcsClient(public_key_id=self.__public_key_id, private_key=self.__private_key,
                                      session_period=self.__session_period, region_id=self.__region_id)
        return self.__acs_client

    def __generate_log_client(self):
        if self.__access_key_id is None:
            self.__access_key_id = config.get_config('account_info', 'access_key_id')
        if self.__access_secret is None:
            self.__access_secret = config.get_config('account_info', 'access_secret')
        if self.__endpoint is None:
            self.__region_id = config.get_config('region_info', 'region_id')
            self.__endpoint = config.get_log_endpoint(self.__region_id)
        print("Generate LogClient with related endpoint : " + self.__endpoint)
        self.__log_client = LogClient(self.__endpoint, self.__access_key_id, self.__access_secret)
        return self.__log_client
