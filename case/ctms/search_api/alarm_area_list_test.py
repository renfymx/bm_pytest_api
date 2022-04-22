'''账单搜索接口'''
import allure
import pytest
import time
from tool.log import logger
from tool.requests_ import Requests
from tool.data_handing import return_data
request = Requests()

data_path=r'D:\bm_pytest_api\data\alarm_area_list_data.yaml'
res_path=r'D:\bm_pytest_api\data\alarm_area_list_res.yaml'

@allure.description('报警数量列表')
@pytest.mark.parametrize('data,res', return_data(data_path,res_path), ids=['区域等级为空','区域编号为空','无区域编号','无区域等级'
])
def test_area_list(data,res,get_token_fixture):
    headers = {
        "token": get_token_fixture
    }
    result = request.get('/alarm/area/list', param=data,headers=headers)
    logger.info(f'接口地址:/alarm/area/list ,请求参数:{data},返回结果:{result}')
    assert result.json()['code'] == res
if __name__ == '__main__':
    pytest.main (["-q"'./alarm_area_list_test.py'])