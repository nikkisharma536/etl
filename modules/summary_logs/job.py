
import os
import datetime
from common.emr_utils import run_on_hive
from config import key_path, ip


if __name__ == '__main__' :
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, "./scripts/summary.hql")

    # run_date = '2019-01-11'
    run_date = datetime.datetime.today().strftime('%Y-%m-%d')

    run_on_hive(file_path, run_date, key_path, ip)

