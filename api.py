import logging

from aiohttp import web
from aiohttp.web_response import json_response


async def github_hook(request):
    return json_response({'ok': True})


async def index(request):
    logging.info(f'Request: {request}')
    return web.Response(text="QEQ")

app = web.Application()
app.router.add_post('/webhook', github_hook)
app.router.add_get('', index)
