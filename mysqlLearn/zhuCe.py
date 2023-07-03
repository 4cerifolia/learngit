# 需求：用户名、密码输入，连接数据库，写入表中
# 登陆：输入用户名、密码，然后在数据表中校验。
# 步骤：
# 1启动MYSQL
# 2终端命令行-创建数据库
# 3终端创建表
# 4代码连接数据库&操作表

import pymysql
from pymysql.cursors import DictCursor


usernm = input('Username:')
userpwd = input('UserPassword:')

# 1 link mysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',passwd='x910823y',charset='utf8mb4',db='usercheck')
cursor = conn.cursor(cursor=DictCursor)

# 2 sql 指令
# 不要用字符串格式化d% format 防止cursor注入
cursor.execute('insert into userlist(username,userpwd)value(%s,%s);',[usernm,userpwd])
conn.commit()

cursor.close()
conn.close()
