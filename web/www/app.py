import logging; logging.basicConfig(level=logging.INFO)
'''
logging记录日志库：
level等级为loggin.DEBUG-->INFO-->WARNING-->ERROR-->CRITICAL
'''
import asyncio
from aiohttp import web

#定义服务器响应请求返回为‘Awesome Website'
async def index(request):
    return web.Response(body=b'<h1>Awesome Website</h1>', content_type='text/html')

#建立服务器应用，持续监听本地9000port的http请求，对手也"/"进行响应
def init():
    app = web.Application()
    app.router.add_get('/', index)
    web.run_app(app, host='127.0.0.1', port=9000)

if __name__ == '__main__':
    init()
