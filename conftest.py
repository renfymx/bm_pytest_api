import pytest
from data.config_data import *
from tool.yaml_ import YamlUsage

@pytest.fixture(scope="session",autouse=True)
def start():
    print('\n打开首页1')
    # flag = 1
@pytest.fixture()
def global_variable():
    '''全局变量配置'''
    variable = {
        'test_ip': TEST_IP,
        # 'downstream_token': DOWNSTREAM_TOKEN,
        # 'upstream_token': UPSTREAM_TOKEN
    }
    return variable
