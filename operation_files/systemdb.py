from modules import folder_check_create as fcc
from modules import check_configuration  as configuration
from modules import archive_bk_files as archive
from os import path

def manage_file(general_dict,sdb_dict):
    msg1 = ''
    output_msg=''
    if sdb_dict['enabled'] == 'true':
        arch_log_path , arch_data_path = fcc.folder_check_cerate(general_dict['target_path'],sdb_dict['name'])
        if general_dict['delete_archive'] == 'true':
            manage_archives.delete_backup_file(general_dict['delete_time'],general_dict['target_path'],sdb_dict['name'])
        if path.exists(arch_log_path):
            if path.exists(sdb_dict['log_file']) and path.exists(sdb_dict['data_file']):
                msg1 = '%s : \n' %(sdb_dict['name'])
                if sdb_dict['action'] == 'mv':
                    msg1=msg1+'\n'+archive.move(sdb_dict['log_file'],arch_log_path)
                if sdb_dict['action'] == 'cp':
                    msg1=msg1+'\n'+archive.copy(sdb_dict['log_file'],arch_log_path)
        if path.exists(arch_data_path):
            if path.exists(sdb_dict['data_file']) and path.exists(sdb_dict['log_file']):
                msg = '%s : \n' %(sdb_dict['name'])
                if sdb_dict['action'] == 'mv':
                    msg1=msg1+'\n'+archive.move(sdb_dict['data_file'],arch_data_path)
                if sdb_dict['action'] == 'cp':
                    msg1=msg1+'\n'+archive.copy(sdb_dict['data_file'],arch_data_path)
        msg = '%s : \n' %(sdb_dict['name'])
        if not path.exists(sdb_dict['log_file']):
            msg=msg + 'log  file path does not exists \n'
        if not path.exists(sdb_dict['data_file']):
            msg=msg + 'data file path does not exists \n'
        
        if msg1=='' : 
            print(msg)
            output_msg=msg
        else : 
            print(msg1)   
            output_msg=msg1
          
    return output_msg