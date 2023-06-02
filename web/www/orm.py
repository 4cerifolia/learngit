# orm=object relational mapping 对象关系映射
# __pool全局变量存储连接池，每个HTTP请求从连接池直接获取数据库链接

import asyncio
import logging
import aiomysql


def log(sql, args=()):
    logging.info('SQL:%s' % sql)


async def creat_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

# 执行SELECT语句，使用select函数，缀加占位符？（sql语句）与%s（mysql语句）的转化
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool)as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?','%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

# INSERT\ UPDATE\ DELETE语句，使用通用的exccute()函数，因为这三者参数相同
async def execute(sql, args):
    log(sql)
    with (await  __pool) as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
        except BaseException as e:
            raise
        return affected


# ORM 映射基类Model
class Model(dict, metaclass=ModelMeataclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return  self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key )

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return  getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field,default) else:field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
            return value
