import os
import logging
import asyncio

from aiohttp import web, ClientSession
from aiohttp.web_response import json_response
from user_map import users


log = logging.getLogger('application')


async def slack_hook(msg):
    log.info(f'Sending msg to slack: {msg}')
    async with ClientSession() as session:
        async with session.post(os.environ.get('SLACK_WEBHOOK_URL'), json={'text': msg}) as response:
            res = await response.text()
            log.info(f'Slack response: {res}')
            return json_response(res)


async def github_hook(request):
    payload = await request.json()
    if payload['action'] == 'review_requested' and payload['requested_reviewer'].get('login'):
        user = payload['requested_reviewer']['login']
        pull_url = payload['pull_request']['html_url']
        reviewer = users.get(user)
        if not reviewer:
            log.info(f'Reviewer name is slack not found: {user}')
        else:
            # asyncio.ensure_future(SlackClient.dispatch(payload['action']))
            asyncio.ensure_future(slack_hook(f'<@{reviewer}> {pull_url}'))
    return json_response({'ok': True})


async def index(request):
    log.info(f'Request: {request}')
    return web.Response(text="It's just test response.")

app = web.Application()
app.router.add_post('/webhook', github_hook)
app.router.add_get('', index)
