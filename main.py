import asyncio
from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, World!")

async def init():
    app = web.Application()
    app.router.add_get('/', handle)
    return app

if True:
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init())
    web.run_app(app, host='localhost', port=8080)
