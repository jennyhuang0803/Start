# Yuntest

Yuntest is a framework for performing behavioral testing on the AliCloud API.

The initial scope of Yuntest covers the core products
https://www.alibabacloud.com/help/zh/doc-detail/62188.htm

- Core : pip install aliyun-python-sdk-core
- VPC : pip install aliyun-python-sdk-vpc
- Log : pip install aliyun-log-python-sdk

You could also use command pip install -r requirements.txt to install all the related package.

Configuration
-------------

Yuntest requires that you have a aliyun sdk configuration file. 

This files should be located in user.home. 
It should be named as aliyun-sdk.conf and formatted as follows

[account_info]
access_key_id=
access_secret=

[new_ak]
public_key_id=
private_key=

[region_info]
region_Id=

Please do not change the section name and key.

Building Yuntest
----------------

The project is built based on Python 2.X and behave which is a BDD testing framework with Python.
Also the project is using PyHamcrest instead of default assert statement.
Please use pip to install related package.

- Behave : pip install behave  //Refer to http://pythonhosted.org/behave/
- PyHamcrest : pip install pyhamcrest  //Refer to https://pypi.python.org/pypi/PyHamcrest

For required python SDK for each products, please refer to https://develop.aliyun.com/tools/sdk?#/python

Command Line Interface (CLI) Usage
----------------------------------
	

Development Guidance
--------------------
