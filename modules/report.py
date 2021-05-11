def daily_report(snd,dev,qua,prd,sdb):
    function_message = ''
    if snd != '' : function_message = function_message+(snd+'\n')
    if dev != '' : function_message = function_message+(dev+'\n')
    if qua != '' : function_message = function_message+(qua+'\n')
    if prd != '' : function_message = function_message+(prd+'\n')
    if sdb != '' : function_message = function_message+(sdb+'\n')
    return function_message