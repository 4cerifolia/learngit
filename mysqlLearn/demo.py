import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='x910823y', charset='utf8',db='day6271')

cursor = conn.cursor()#create 游标


# create table
# sql = '''
# create table tb5(
# id int not null auto_increment primary key,
# email varchar(16) not null,
# age int default 0
# )default charset=utf8;'''
# cursor.execute(sql)
# conn.commit()
# show tables;
# creat table table_name(
# lineName1 type1, 
# lineName2 type2
# )default charset=utf8;

# # 删除表
# cursor.execute('drop table tb1;')
# conn.commit()

# # 清空表
# cursor.execute('delete from tb5;')
# conn.commit()

#
#cursor.execute('drop database day07;')
#conn.commit() # 确认键入

#cursor.execute('show databases;')
#result = cursor.fetchall()

#print(result)# 1.查看数据库


# 数据行管理
# 增删改查
# 1.增
# insert into tb5(name,email,age) value('x','x',19);
# 2.查
# select * from tb5 where age=9;
# 3.删
# delete from tb5 where age=9;
# 4.改
# update tb5 set age=20 where id=8;





# 2.关闭游标
cursor.close()
conn.close()