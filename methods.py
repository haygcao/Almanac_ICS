# Almanac methods pool
# By Clok Much


# pzbj = pzbj_original[index]['pzbj']

import config
from json import load as load_json


def get_details():
    """
    解析宜忌和彭祖百忌为一个列表
    :return:
    """
    result = []
    file_object_yj = open(file=config.Default.yj, mode='rb')
    file_object_pzbj = open(file=config.Default.other, mode='rb')
    yj_original = load_json(file_object_yj)
    pzbj_original = load_json(file_object_pzbj)
    for month in config.MonthDate.large_month:
        for date in range(1, 32):
            date = str(date)
            if len(date) == 1:
                date = "0" + date
            index = month + date
            yi = yj_original["d" + index]['y']
            ji = yj_original["d" + index]['j']
            pzbj = ""
            tmp0 = "宜：" + yi + "\\n" + "忌：" + ji + "" + pzbj
            tmp1 = config.Default.year + month + date
            tmp2 = (tmp1, tmp0)
            result.append(tmp2)
    for month in config.MonthDate.small_month:
        for date in range(1, 31):
            date = str(date)
            if len(date) == 1:
                date = "0" + date
            index = month + date
            yi = yj_original["d" + index]['y']
            ji = yj_original["d" + index]['j']
            pzbj = ""
            tmp0 = "宜：" + yi + "\\n" + "忌：" + ji + "" + pzbj
            tmp1 = config.Default.year + month + date
            tmp2 = (tmp1, tmp0)
            result.append(tmp2)
    for month in config.MonthDate.special_month:
        if int(config.Default.year) % 4 == 0:
            end_range = 30
        else:
            end_range = 29
        for date in range(1, end_range):
            date = str(date)
            if len(date) == 1:
                date = "0" + date
            index = month + date
            yi = yj_original["d" + index]['y']
            ji = yj_original["d" + index]['j']
            pzbj = ""
            tmp0 = "宜：" + yi + "\\n" + "忌：" + ji + "" + pzbj
            tmp1 = config.Default.year + month + date
            tmp2 = (tmp1, tmp0)
            result.append(tmp2)
    result.sort()
    return result

