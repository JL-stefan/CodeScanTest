import pyodbc  
import threading  
import time  
  
# 数据库连接字符串（请根据实际情况修改）  
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server;DATABASE=your_database;UID=your_username;PWD=your_password'  
  
# 创建数据库连接  
conn = pyodbc.connect(conn_str)  
cursor = conn.cursor()  
  
# 定义调用存储过程的函数  
def call_procedure(proc_name, param1, param2):  
    try:  
        cursor.execute(f"{{CALL {proc_name}(?, ?)}}", param1, param2)  
        conn.commit()  
        print(f"{proc_name} completed successfully.")  
    except pyodbc.Error as e:  
        print(f"{proc_name} encountered an error: {e}")  
        conn.rollback()  
  
# 创建并启动线程来调用存储过程  
thread1 = threading.Thread(target=call_procedure, args=('Procedure1', 1, 'NewValue1'))  
thread2 = threading.Thread(target=call_procedure, args=('Procedure2', 2, 'NewValue2'))  
  
# 几乎同时启动两个线程  
thread1.start()  
time.sleep(0.1)  # 稍微延迟一下以模拟“几乎同时”  
thread2.start()  
  
# 等待线程完成  
thread1.join()  
thread2.join()  
  
# 关闭数据库连接  
cursor.close()  
conn.close()
