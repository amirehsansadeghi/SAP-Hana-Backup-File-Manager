from modules import folder_check_create as fcc
from modules import check_configuration  as configuration
from modules import archive_bk_files as archive
from modules import manage_archives
from os import path

def manage_file(general_dict,snd_dict):
    msg1 = ''
    output_msg=''
    if snd_dict['enabled'] == 'true':
        arch_log_path , arch_data_path = fcc.folder_check_cerate(general_dict['target_path'],snd_dict['name'])
        if general_dict['delete_archive'] == 'true':
            manage_archives.delete_backup_file(general_dict['delete_time'],general_dict['target_path'],snd_dict['name'])
        if path.exists(arch_log_path):
            if path.exists(snd_dict['log_file']) and path.exists(snd_dict['data_file']):
                msg1 = '%s :\n' %(snd_dict['name'])
                if snd_dict['action'] == 'mv':
                    msg1=msg1+archive.move(snd_dict['log_file'],arch_log_path)
                if snd_dict['action'] == 'cp':
                    msg1=msg1+archive.copy(snd_dict['log_file'],arch_log_path)
        if path.exists(arch_data_path):
            if path.exists(snd_dict['data_file']) and path.exists(snd_dict['log_file']):
                msg = '%s :\n' %(snd_dict['name'])
                if snd_dict['action'] == 'mv':
                    msg1=msg1+'\n'+archive.move(snd_dict['data_file'],arch_data_path)
                if snd_dict['action'] == 'cp':
                    msg1=msg1+'\n'+archive.copy(snd_dict['data_file'],arch_data_path)
        msg = '%s : \n' %(snd_dict['name'])
        if not path.exists(snd_dict['log_file']):
            msg=msg + 'log  file path does not exists \n'
        if not path.exists(snd_dict['data_file']):
            msg=msg + 'data file path does not exists \n'
        if msg1=='' : 
            output_msg=msg
        else : 
            output_msg=msg1  
    return output_msg