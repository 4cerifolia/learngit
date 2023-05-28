#orm=object relational mapping 对象关系映射
#__pool全局变量存储连接池，每个HTTP请求从连接池直接获取数据库链接

import asyncio, logging, aiomysql


def log(sql, args = ()):
    logging.info('SQL:%s' % sql)

async def creat_pool(loop, **kw):
    logging.info('create database connection pool...')
    global  __pool
    __pool = await  aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db'],
        charset = kw.get('charset','utf-8'),
        auto
    )