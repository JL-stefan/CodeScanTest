import sqlite3  
  
def get_user_by_username(username):  
    # 假设我们有一个SQLite数据库  
    conn = sqlite3.connect('example.db')  
    cursor = conn.cursor()  
      
    # 这里的SQL查询存在SQL注入漏洞  
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
      
    result = cursor.fetchone()  
    conn.close()  
      
    return result  
  
# 假设用户输入了恶意的用户名  
malicious_username = "' OR '1'='1"  
user = get_user_by_username(malicious_username)  
print(user)

def memory_leak():  
    leaky_list = []  
    while True:  
        leaky_list.append("some data")  # 不断向列表添加数据，但不删除旧数据  
        # 注意：在实际应用中，应该有一个机制来清理不再需要的数据

import os  
  
def execute_command(command):  
    # 这里的代码存在命令注入漏洞  
    os.system(command)  
  
# 假设用户输入了恶意的命令  
malicious_command = "; rm -rf /"  # 这是一个非常危险的命令，会删除根目录下的所有文件和文件夹  
execute_command("ls " + malicious_command)
