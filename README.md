# Blist API Wrapper for Python

## Table of contents

1. [Getting started](#getting-started)
2. [Installing](#installing)
3. [Creating a `Blist` instance](#creating-a-blist-instance)
4. [Using webhooks](#using-webhooks)
5. [Reference](#reference)

## Getting started

This is the documentation for the Blist API wrapper written in Python. You'll want to make sure to check out the [table of contents](#table-of-contents) for information on installing and getting the Blist API wrapper working correctly. You need to be using [discord.py](https://github.com/Rapptz/discord.py) and be using the bot commands extension in your project to be able to use this API wrapper.

## Installing

**It is assumed that you have basic knowledge of using the command line and using PyPi (`pip`).**

1. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) for installing the package and then proceed to activate the virtual environment.
2. Run `pip install -U blistpy`. This will install everything required to make the package work.
3. Congratulations, you've completed the installation of the Blist API wrapper.

## Creating a `Blist` instance

Import the Blist wrapper by putting `import blist` at the top of your main bot file. This will import the wrapper into the file so you can start using it.

Once you have imported the wrapper, you need to create an instance of `Blist`. `Blist` takes a `Bot` or `AutoShardedBot` instance and your Blist API token. It should look something like below. You can omit `token="your blist token"` if you don't need to make any authorized requests.

```py
import blist

blist_api = blist.Blist(bot, token="your blist token")
```

It's time to begin making requests. Check out the [reference](#reference) for a full list of methods.

## Using webhooks

In Blist, webhooks are used to send a request to your server whenever your bot is upvoted. This can be utilized in many ways, usually for vote locking without having to constantly poll the server to see if someone has upvoted the bot.

You can easily setup a webhook server by using the included server. The code below creates an instance of `WebhookServer` and runs it. Once you run it, whenever a user upvotes your bot, an `on_blist_vote` event will be fired containing the user ID of the user and the time they upvoted it.

### Run webhook server

```py
import blist

blist_api = blist.Blist(bot, token="your blist token")

webhook = blist.WebhookServer(blist_api)

await webhook.run()
```

### Receive vote event

```py
# Outside of a cog

@bot.event
async def on_blist_vote(user_id, time):
    # process upvote
    pass

# Inside of a cog

@commands.Cog.listener()
async def on_blist_vote(self, user_id, time):
    # process upvote
    pass
```

### Close webhook server

```py
import blist

blist_api = blist.Blist(bot, token="your blist token")

webhook = blist.WebhookServer(blist_api)

await webhook.run()

await webhook.close()
```

## Reference

### `blist.Blist(bot, token=None)`

Client interface for interacting with the entire Blist API.

**Parameters**

+ **bot** (`commands.Bot`) — Discord bot instance to be used with the API.
+ **token** (Optional[`str`]) — Blist API token. This isn't required if you do not need authorization.

---

### `await blist.Blist.fetch_bot(bot_id=None)`

*This method is a coroutine.*

Fetches information about a bot. Does not require authorization.

**Parameters**

+ **bot_id** (Optional[`int`]) — The ID of the bot to fetch information about. Defaults to the current bot.

**Raises**

`blist.errors.UnknownBot` — The bot was not found on the list.

**Returns**

|Attribute|Type|Description|
|---|---|---|
|id|`int`|Bot ID|
|name|`str`|Name of the bot|
|main_owner|`int`|ID of the main owner of the bot|
|owners|`str`|The secondary bot owner IDs|
|library|`str`|The library the bot was programmed in|
|website|`str`|Link to the bot's website|
|github|`str`|Link to the bot's GitHub repository|
|short_description|`str`|Short description of the bot|
|long_description|`str`|Long description of the bot|
|prefix|`str`|The bot's prefix|
|invite_url|`str`|Link to the invite URL of the bot|
|support_server|`str`|Bot support guild invite code|
|tags|List[`str`]|List of bot tags on the Blist website|
|monthly_votes|`int`|Amount of votes the bot has gotten within a month|
|total_votes|`int`|Amount of votes the bot has gotten in all time|
|certified|`bool`|Whether the bot is certified on the Blist website|
|vanity_url|`str`|The vanity URL to the bot on the Blist website|
|server_count|`int`|Amount of guilds the bot is in|
|shard_count|`int`|Amount of shards the bot is using|
|joined|`datetime.datetime`|The date the bot was added to the Blist website|
|invites|`int`|Amount of times the bot has been invited from the Blist website|
|page_views|`int`|Amount of views the bot page has received|
|donate_url|`str`||Link to the bot's donate page|
|avatar_hash|`str`|The bot avatar hash|
|privacy_policy_url|`str`|Link to the bot's privacy policy URL|
|status|`str`|The bot's current status|

**Return Type**

`blist.models.Bot`

---

### `await blist.Blist.post_bot_stats()`

*This method is a coroutine.*

Posts bot statistics to the Blist website. Requires authorization.

**Raises**

`blist.errors.InvalidData` — Invalid guild or shard count sent to the server. Normally, you will not receive this.

`blist.errors.InvalidAuthorization` — Invalid token provided or you did not specify a token.

`blist.errors.UnknownBot` — The bot was not found on the list.

---

### `await blist.Blist.fetch_user_info(user_id)`

*This method is a coroutine.*

Fetches information about a user. Does not require authorization.

**Parameters**

+ **user_id** (`int`) — The ID of the user to fetch information about.

**Raises**

`blist.errors.InvalidData` — The user ID must be an `int`.

`blist.errors.UnknownUser` — The user's account was not found on the list.

**Returns**

|Attribute|Type|Description|
|---|---|---|
|id|`int`|User ID|
|bio|`str`|User's biography|
|staff|`bool`|Whether the user is staff|
|joined_at|`datetime.datetime`|The date the user created an account on the Blist website|
|reddit|`str`|The user's Reddit username|
|snapchat|`str`|The user's Snapchat username|
|instagram|`str`|The user's Instagram username|
|twitter|`str`|The user's Twitter handle|
|github|`str`|The user's GitHub username|
|website|`str`|Link to the user's website|
|bots|`int`|Amount of bots the user has on the Blist website|

**Return Type**

`blist.models.User`

---

### `await blist.Blist.fetch_bot_votes()`

*This method is a coroutine.*

Fetches monthly and total votes. This also returns users who have voted for your bot. Requires authorization.

**Raises**

`blist.errors.InvalidAuthorization` — Invalid token provided or you did not specify a token.

`blist.errors.UnknownBot` — The bot was not found on the list.

**Returns**

**`blist.models.Votes`**

|Attribute|Type|Description|
|---|---|---|
|monthly|`int`|Amount of votes the bot has gotten within a month|
|total|`int`|Amount of votes the bot has gotten in all time|
|votes|List[`blist.models.Vote`]|List of users who have voted for your bot and the time they did so|

**`blist.models.Vote`**

|Attribute|Type|Description|
|---|---|---|
|userid|`int`|The ID of the user who voted|
|time|`datetime.datetime`|The timestamp of when the user voted|

**Return Type**

`blist.models.Votes`

---

### `await blist.Blist.fetch_bot_widget(bot_id=None, widget_type="normal")`

*This method is a coroutine.*

Fetches the widget for the bot. The widget is an image. Does not require authorization.

**Parameters**

+ **bot_id** (Optional[`int`]) — The ID of the bot to fetch the widget for. Defaults to the current bot.
+ **widget_type** (Optional[`str`]) — Type of widget to fetch. Currently, `normal` is the only widget type.

**Raises**

`blist.errors.UnknownBot` — The bot was not found on the list.

**Returns**

`bytes` like object. You must use [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO) to send the image through Discord.

**Return Type**

`bytes`

---

### `await blist.Blist.close()`

*This method is a coroutine.*

Disallows the `blist.Blist` instance from being used to make anymore requests to the API.

**Note:** You must run this when stopping your bot.

---

### `blist.WebhookServer(blist, port=8000)`

Server for receiving upvote events and dispatching them.

**Parameters**

+ **blist** (`blist.Blist`) — An instance of `Blist`. You **must** have an API token specified.
+ **port** (`int`) — The port to run the server on. Defaults to `8000`.

**Dispatch Event**

`on_blist_vote`

**Dispatch Parameters**

+ **user_id** (`int`) — The ID of the user who upvoted the bot.
+ **time** (`datetime.datetime`) — The timestamp of when the user upvoted the bot.

---

### `await blist.WebhookServer.run()`

*This method is a coroutine.*

Starts the webhook server and allows it to serve requests.

**Note:** You do not need to run this method in a task, everything is handled for you.

---

### `await blist.WebhookServer.close()`

*This method is a coroutine.*

Stops the webhook server and disallows it from serving requests.

**Note:** You must run this when stopping your bot if the server is currently running.