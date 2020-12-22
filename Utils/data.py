import json
import os


class Data:
    @classmethod
    def get_json_data(cls, file, father_key="", son_key=""):
        """
        :param file: ./Data目录下
        :param father_key: 父key
        :param son_key: 子key list
        :return:
        """
        all_list = []
        with open("./Data" + os.sep + file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if father_key:
                if son_key:
                    value = data.get(father_key)
                    for i in value:
                        lis = []
                        for o in son_key:
                            lis.append(i.get(o))
                        all_list.append(tuple(lis))
        return all_list
