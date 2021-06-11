from aiohttp import web
from .api import Blist
import datetime

class WebhookServer:
    def __init__(self, blist: Blist, port: int = 8000):
        self.bot = blist.bot
        self.token = blist.token
        self.port = port

        self._app = web.Application(loop=self.bot.loop)
        self._app.add_routes([web.post("/callback", self._process_request)])

    async def _process_request(self, request: web.Request) -> web.Response:
        if request.headers.get("Authorization") != self.token:
            return web.Response(status=403)

        json = await request.json()

        user_id = json.get("user")
        time = datetime.datetime.fromtimestamp(json.get("time"))

        self.bot.dispatch("blist_vote", user_id, time)

        return web.Response(status=204)

    async def run(self):
        self._runner = web.AppRunner(self._app)
        await self._runner.setup()
        site = web.TCPSite(self._runner, "0.0.0.0", self.port)
        await site.start()

    async def close(self):
        await self._runner.cleanup()