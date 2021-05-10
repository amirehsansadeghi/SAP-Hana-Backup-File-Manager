import shutil
import os 
from modules import get_time_date

def move(source,destination):
    count=0
    files_name = os.listdir(source)
    for file_name in files_name:
        src=source+file_name
        shutil.move(src,destination)
        count=count+1
    get_date = get_time_date.get_time_date()
    get_time = get_time_date.get_system_time()
    status = 'Success'
    msg = '''at the %s %s time, all files is %i and moved %i files from %s to %s \033[32m %s \x1b[0m
    ''' %(get_date,get_time,file_count,count,source,destination,status)

def copy(source,destination):
    count=0
    file_names = os.listdir(source)
    for file_name in file_names:
        src = source+file_name
        shutil.copy(src,destination)
        count=count+1
    file_count = len(file_names)
    get_date = get_time_date.get_time_date()
    get_time = get_time_date.get_system_time()
    status = 'Success'
    msg = '''at the %s %s time, all files is %i and copied %i files from %s to %s \033[32m %s \x1b[0m
    ''' %(get_date,get_time,file_count,count,source,destination,status)
    return msg    

            
