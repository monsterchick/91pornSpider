import re


def avoid_spc_char(folder_name):
    # 过滤特殊字符
    folder_name = re.sub('[\/:*?"<>|]', '', folder_name)
    return folder_name