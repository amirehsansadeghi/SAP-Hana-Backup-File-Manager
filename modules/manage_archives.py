from modules import get_time_date 
import os 
import shutil

def delete_backup_file(week,path,sid):
    bk_path = path + sid
    last_month_date=get_time_date.get_last_month(week)
    bk_path = bk_path+'/'+last_month_date
    if os.path.exists(bk_path)  :         
        shutil.rmtree(bk_path)