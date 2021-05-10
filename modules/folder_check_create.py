import configparser
import os 
from modules import get_time_date


def folder_check_cerate(path,sid_name):
    folder_name = get_time_date.get_time_date()
    try:
        if path[-1] != '/':
            path=path+'/'
        if not os.path.isdir(path+sid_name):
            os.makedirs(path+sid_name)    
       
        if os.path.isdir(path+sid_name):
            if not os.path.isdir(path+sid_name+'/'+folder_name):
                os.makedirs(path+sid_name+'/'+folder_name)
            
        
        if os.path.isdir(path+sid_name+'/'+folder_name):
            if not os.path.isdir(path+sid_name+'/'+folder_name+'/log'):
                if not os.path.isdir(path+sid_name+'/'+folder_name+'/data'):
                    os.makedirs(path+sid_name+'/'+folder_name+'/log')
                    os.makedirs(path+sid_name+'/'+folder_name+'/data')
        log_file_path= path+sid_name+'/'+folder_name+'/log'
        data_file_path = path+sid_name+'/'+folder_name+'/data'
        return log_file_path , data_file_path
    except:
        print('please check taget path , maybe folder has been duplicated')