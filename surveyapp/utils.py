# coding:UTF-8

import hashlib
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings


# 由于系统设计缺陷，故在数据字典这里做一个code与name映射
def dataDic():
    return {
    "110":"acdc",
    "135":"air_smooth",
    "112":"airconditioning_type",
    "124":"airconditioning_type",
    "132":"brand",
    "125":"building_structure",
    "126":"chamfer",
    "129":"device_type",
    "130":"direction_of_air_supply",
    "128":"floor_format",
    "127":"floor_type",
    "131":"function",
    "116":"inAirSort",
    "123":"inoutsort",
    "111":"mode",
    "117":"outAirSort",
    "133":"out_airconditioning_type",
    "137":"pass_type",
    "113":"plot",
    "119":"power_supply_type",
    "118":"publicPass",
    "115":"rackPlot",
    "136":"shelter",
    "114":"supplyMode",
    "134":"west_facing",
    "138":"task_state",
    "122":"layingsort",
    }

def md5Util(sourse):
    hash = hashlib.md5()
    hash.update(sourse.encode('latin1'))
    return hash.hexdigest()

def djGenPwd(sourse):
    dj_ps = make_password(sourse, None, 'pbkdf2_sha256')
    print(dj_ps)
    return dj_ps

def djCheckPwd(sourse, pwd):
    ps_bool = check_password(sourse, pwd)
    print(ps_bool)
    return ps_bool


if __name__ == '__main__':
    # 当在文件内调用时需要调用一下settings.configure()。同时在setting.py中配置好PASSWORD_HASHERS
    settings.configure()
    djCheckPwd('admin', 'pbkdf2_sha256$100000$t3RhcPPcJT2u$VesauRl4SwE1+ZoKsc1ext3IluVBfYPtzhb1COAe304=')






