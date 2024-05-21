import mysql.connector
import uuid,os
from dotenv import load_dotenv
import json
import time

load_dotenv()

config = {
    'user': 'root',
    'password': os.getenv('mysqlpassword'),
    'host': '127.0.0.1',
    'database': 'mydb',
    'raise_on_warnings': True
}

## 生成并插入一条uuid到数据库
def genRefercode(uuid,status):
    
    if 1==1:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        
        # 插入数据的SQL语句
        insert_query = """
        INSERT INTO refercode (uuid, status)
        VALUES (%s, %s)
        """
        
        # 插入数据
        cursor.execute(insert_query, (uuid, status))
        
        # 提交事务
        cnx.commit()
        
        print("数据插入成功，UUID:", uuid)


## 检查refercode状态，如果存在则消费它.
def checkRefercode(refer_uuid):
    if 1==1:
        # 连接到MySQL数据库
        cnx = mysql.connector.connect(**config)
        
        cursor = cnx.cursor()
        
        # 查询数据的SQL语句
        query = """
        SELECT status FROM refercode WHERE uuid = %s
        """
        
        # 执行查询
        cursor.execute(query, (refer_uuid,))
        result = cursor.fetchone()
        
        # 检查结果
        if result and result[0] == 0:
            print("Exists:"+refer_uuid)
            consumeRefercode(refer_uuid)
            return True
        else:
            print("UUID已经消费")
            return False
    print("UUID不存在或已经消费")
    return False

## 表示已经消费了这个字段.
def consumeRefercode(refer_uuid):
    if 1==1:
        # 连接到MySQL数据库
        cnx = mysql.connector.connect(**config)
        
        cursor = cnx.cursor()
        
        # 更新数据的SQL语句
        update_query = """
        UPDATE refercode
        SET status = 1
        WHERE uuid = %s
        """
        cursor.execute(update_query, (refer_uuid,))
        cnx.commit()
        if cursor.rowcount > 0:
            print("UUID对应的status字段已消费。")
        else:
            print("未找到对应的UUID，无法更新。")

def genUuid():
    random_uuid = uuid.uuid4()
    genRefercode(str(random_uuid),"0")
    print("生成的UUID:", random_uuid)
    return(random_uuid)

## 生成新Uuid
# genUuid()

## 检查并且消费
checkRefercode("49a9939a-91a7-4d88-84ad-d2e4a5d92aab")
