import os
from ruamel import yaml

class YamlUsage:
    def __init__(self,file_path):
        self.file_path=file_path
    def write_yaml(self,data,mode):
        self.__check()
        file = open(self.file_path, mode, encoding='utf-8')
        yaml.dump(data, file, Dumper=yaml.RoundTripDumper)
        file.close()
    def read_yaml(self):
        self.__check()
        file = open(self.file_path, 'r', encoding='utf-8')
        with file as doc:
            content = yaml.load(doc, Loader=yaml.Loader)
            return content
    def __check(self):
        if os.path.exists(self.file_path):
            pass
        else:
            file = open(self.file_path, 'w')
            file.close()
if __name__ == '__main__':

    # y =YamlUsage(r'F:\bm_api\data\rr1.yaml')
    # y.write_yaml({1:1},'a')
    #在这里写入了测试bill_search_test.py文件的数据，也可以手动直接再yaml文件里写
    # yml = YamlUsage(r'D:\bm_pytest_api\data\bill_search_data.yaml')
    # data1 = {
    #     "billCommonNo": "",
    #     "status": None,
    #     "makeBillStatus": None,
    #     "projectNos": [],
    #     "commonCompanyName": "",
    #     "year": "2022",
    #     "month": "07",
    #     "billType": "UP",
    #     "size": 20,
    #     "page": 1
    # }
    # data2 = {
    #     "billCommonNo": "",
    #     "status": None,
    #     "makeBillStatus": None,
    #     "projectNos": ['320SF000206003'],
    #     "commonCompanyName": "",
    #     "year": "2022",
    #     "month": "07",
    #     "billType": "UP",
    #     "size": 20,
    #     "page": 1
    # }
    # data3 = {
    #     "billCommonNo": "",
    #     "status": 'RECONCILIATIONING',
    #     "makeBillStatus": None,
    #     "projectNos": [],
    #     "commonCompanyName": "",
    #     "year": "2022",
    #     "month": "07",
    #     "billType": "UP",
    #     "size": 20,
    #     "page": 1
    # }
    # data=[data1,data2,data3]
    # yml.write_yaml(data,'a')
    # print(yml.read_yaml())

    def return_data():
        yml = YamlUsage(r'D:\bm_pytest_api\data\alarm_area_list_data.yaml')
        data_yml = yml.read_yaml()
        yml_r = YamlUsage(r'D:\bm_pytest_api\data\alarm_area_list_res.yaml')
        res_yml = yml_r.read_yaml()
        points_tulpe = list(zip(data_yml, res_yml))
        return points_tulpe



    print(return_data())

