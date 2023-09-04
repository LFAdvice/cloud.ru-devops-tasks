from aiohttp import web
import getpass
import os
import uuid
import socket

HOSTNAME = socket.gethostname()
AUTHOR = os.getenv('AUTHOR', default=getpass.getuser())
ID = os.getenv('ID', default='id unavailable')

async def get_hostname(request):
    return web.Response(text=HOSTNAME)

async def get_author(request):
    return web.Response(text=AUTHOR)

async def get_id(request):
    return web.Response(text=str(ID))

async def get_healthz(request):
    return web.Response(text="still alive")

app = web.Application()
app.add_routes([web.get('/hostname', get_hostname)])
app.add_routes([web.get('/author', get_author)])
app.add_routes([web.get('/id', get_id)])
app.add_routes([web.get('/healthz', get_healthz)])

web.run_app(app, port=8000)