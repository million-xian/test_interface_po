import yaml

def read_yaml(file):
    """
    读取yaml文件，返回所有values
    :param file: yaml文件路径
    :return: values
    """
    arr = []
    #获取文件流
    with open(file,"r",encoding="utf-8") as f:
        #遍历values
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
    return arr


def read_yaml2(file):
    """
    读取yaml文件,返回所有key:values
    :return:返回yaml文件数据，格式为列表
    """
    with open(file,encoding="utf-8") as y:
        return yaml.load(y,Loader=yaml.FullLoader)

if __name__=="__main__":
    data = read_yaml("../data/testcase2.yaml")
    print(data)

