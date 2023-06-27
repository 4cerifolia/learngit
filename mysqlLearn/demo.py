import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='x910823y', charset='utf8')
cursor = conn.cursor()#create 游标



# show tables;
# creat table table_name(
# lineName1 type1, 
# lineName2 type2
# )default charset=utf8;



#
#cursor.execute('drop database day07;')
#conn.commit() # 确认键入

#cursor.execute('show databases;')
#result = cursor.fetchall()

#print(result)# 1.查看数据库

# 2.关闭游标
cursor.close()
conn.close()