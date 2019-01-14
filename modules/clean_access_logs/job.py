#1. Read the script file
#2. Generate temp s3 path with uuid generator
#3. save the script file on s3 path
#4. ssh and execute hive script
#5. delete hive script from s3

import os
import datetime
from common.emr_utils import run_on_hive
from config import key_path, ip


if __name__ == '__main__' :
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, "./scripts/incremental_etl_with_param.hql")

    # run_date = '2019-01-11'
    run_date = datetime.datetime.today().strftime('%Y-%m-%d')

    run_on_hive(file_path, run_date, key_path, ip)

