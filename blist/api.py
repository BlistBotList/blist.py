import aiohttp
from . import models
from . import errors
import typing

class Blist:
    def __init__(self, bot, token: typing.Optional[str] = None):
        self.bot = bot
        self.token = token
        self._session = aiohttp.ClientSession(loop=self.bot.loop)

        self.BASE_URL = "https://blist.xyz/api/v2"

    async def fetch_bot(self, bot_id: typing.Optional[int] = None) -> models.Bot:
        if bot_id is None:
            bot_id = self.bot.user.id

        response = await self._session.get(f"{self.BASE_URL}/bot/{bot_id}/")
        json = await response.json()

        if response.status == 200:
            return models.Bot(**json)

        if response.status == 404:
            raise errors.UnknownBot()
        else:
            raise errors.HTTPException(response, json.get("detail"))

    async def post_bot_stats(self):
        if self.token is None:
            raise errors.InvalidAuthorization()

        headers = {
            "Authorization": self.token
        }
        payload = {
            "server_count": len(self.bot.guilds),
            "shard_count": self.bot.shard_count or 1
        }

        response = await self._session.patch(f"{self.BASE_URL}/bot/{self.bot.user.id}/stats/", headers=headers, json=payload)

        if response.status == 204:
            return
        
        json = await response.json()
        
        if response.status == 400:
            raise errors.InvalidData(json.get("detail"))
        elif response.status == 403:
            raise errors.InvalidAuthorization()
        elif response.status == 404:
            raise errors.UnknownBot()
        else:
            raise errors.HTTPException(response, json.get("detail"))

    async def fetch_user_info(self, user_id: int) -> models.User:
        if user_id == self.bot.user.id:
            raise errors.UnknownUser()

        response = await self._session.get(f"{self.BASE_URL}/user/{user_id}/")
        json = await response.json()

        if response.status == 200:
            return models.User(**json)

        if response.status == 400:
            raise errors.InvalidData(json.get("detail"))
        elif response.status == 404:
            raise errors.UnknownUser()
        else:
            raise errors.HTTPException(response, json.get("detail"))

    async def fetch_bot_votes(self) -> models.Votes:
        if self.token is None:
            raise errors.InvalidAuthorization()

        headers = {
            "Authorization": self.token
        }

        response = await self._session.get(f"{self.BASE_URL}/bot/{self.bot.user.id}/votes/", headers=headers)
        json = await response.json()

        if response.status == 200:
            return models.Votes(**json)

        if response.status == 403:
            raise errors.InvalidAuthorization()
        elif response.status == 404:
            raise errors.UnknownBot()
        else:
            raise errors.HTTPException(response, json.get("detail"))

    async def fetch_bot_reviews(self) -> models.Reviews:
        if self.token is None:
            raise errors.InvalidAuthorization()

        headers = {
            "Authorization": self.token
        }

        response = await self._session.get(f"{self.BASE_URL}/bot/{self.bot.user.id}/reviews/", headers=headers)
        json = await response.json()

        if response.status == 200:
            return models.Reviews(**json)

        if response.status == 403:
            raise errors.InvalidAuthorization()
        elif response.status == 404:
            raise errors.UnknownBot()
        else:
            raise errors.HTTPException(response, json.get("detail"))

    async def close(self):
        await self._session.close()
