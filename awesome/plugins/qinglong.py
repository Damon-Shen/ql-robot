from nonebot import on_command, CommandSession
import re
import requests
import json
import sqlite3

# on_command 装饰器将函数声明为一个命令处理器
# 这里 qinglong 为命令的名字，同时允许使用别名「青龙」
@on_command('qinglong', aliases=('青龙'), permission=lambda s: s.is_superuser)
async def qinglong(session: CommandSession):
    qinglong_config = []
    qinglong_address = (await session.aget(prompt='请输入青龙服务地址')).strip()
    
    if qinglong_address:
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        qinglong_address = re.findall(pattern,qinglong_address)
        while not qinglong_address:
            qinglong_address = (await session.aget(prompt='青龙服务地址有误，请重新输入')).strip()
        qinglong_config.append(qinglong_address[0])
        qinglong_client_id = (await session.aget(prompt='请输入青龙Client ID')).strip()
        while not qinglong_client_id:
             qinglong_client_id = (await session.aget(prompt='请输入青龙Client ID')).strip()
        qinglong_config.append(qinglong_client_id)
        qinglong_client_secret = (await session.aget(prompt='请输入青龙Client Secret')).strip()
        while not qinglong_client_secret:
            qinglong_client_secret = (await session.aget(prompt='请输入青龙Client Secret')).strip()
        qinglong_config.append(qinglong_client_secret)
                  
    qinglong_report = await set_qinglong_config(qinglong_config)

   
    await session.send(qinglong_report)


async def set_qinglong_config(config: list) -> list:
   
    url = config[0] + "/open/auth/token?client_id=" + config[1] + "&client_secret=" + config[2]
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get(url=url, headers=headers)
        token = json.loads(res.text)["data"]['token']
        
    except:
        return '连接青龙服务失败，请确认所有信息填写正确!'
    else:
        conn = sqlite3.connect('config.sqlite')
        
        create_tb_cmd='''
            CREATE TABLE IF NOT EXISTS qinglong
            (id INT,
            address TEXT,
            client_id TEXT,
            client_secret TEXT,
            token TEXT);
            '''
        conn.execute(create_tb_cmd)
        conn.commit()

        select_db_cmd = '''
        SELECT * FROM qinglong;
        '''
        cu=conn.cursor()
        cu.execute(select_db_cmd)
        config_data = cu.fetchall()
        if len(config_data)>0:
            update_db_cmd = f'''
            UPDATE qinglong set address="{config[0]}",client_id="{config[1]}",client_secret="{config[2]}",token="{token}" where id=1;
            '''
            conn.execute(update_db_cmd)
            conn.commit()

        else:
            insert_db_cmd=f'''
            INSERT INTO qinglong (id,address,client_id,client_secret,token) VALUES (1,"{config[0]}","{config[1]}","{config[2]}","{token}");
            '''
            conn.execute(insert_db_cmd)
            conn.commit()
        conn.close()
        return '连接青龙服务成功!'


    