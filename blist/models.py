import typing
import datetime

class Bot:
    def __init__(self, **kwargs):
        self.id: int = kwargs.get("id")
        self.name: str = kwargs.get("name")
        self.main_owner: int = kwargs.get("main_owner")
        self.owners: str = kwargs.get("owners")
        self.library: str = kwargs.get("library")
        self.website: str = kwargs.get("website")
        self.github: str = kwargs.get("github")
        self.short_description: str = kwargs.get("short_description")
        self.long_description: str = kwargs.get("long_description")
        self.prefix: str = kwargs.get("prefix")
        self.invite_url: str = kwargs.get("invite_url")
        self.support_server: str = kwargs.get("support_server")
        self.tags: typing.List[str] = kwargs.get("tags")
        self.monthly_votes: int = kwargs.get("monthly_votes")
        self.total_votes: int = kwargs.get("total_votes")
        self.certified: bool = kwargs.get("certified")
        self.vanity_url: str = kwargs.get("vanity_url")
        self.server_count: int = kwargs.get("server_count")
        self.shard_count: int = kwargs.get("shard_count")
        self.add_date: datetime.datetime = datetime.datetime.fromisoformat(kwargs.get("joined").strip("Z"))
        self.invites: int = kwargs.get("invites")
        self.page_views: int = kwargs.get("page_views")
        self.donate_url: str = kwargs.get("donate_url")
        self.avatar_hash: str = kwargs.get("avatar_hash")
        self.privacy_policy_url: str = kwargs.get("privacy_policy_url")
        self.status: str = kwargs.get("status")

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} name='{self.name}' prefix='{self.prefix}' library='{self.library}'>"

class User:
    def __init__(self, **kwargs):
        self.id: int = kwargs.get("id")
        self.bio: str = kwargs.get("bio")
        self.staff: bool = kwargs.get("staff")
        self.joined_at: datetime.datetime = datetime.datetime.fromtimestamp(kwargs.get("joined_at"))
        self.reddit: str = kwargs.get("reddit")
        self.snapchat: str = kwargs.get("snapchat")
        self.instagram: str = kwargs.get("instagram")
        self.twitter: str = kwargs.get("twitter")
        self.github: str = kwargs.get("github")
        self.website: str = kwargs.get("website")
        self.bots: int = kwargs.get("bots")

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} bio='{self.bio}' staff={self.staff} bots={self.bots}>"

class Vote:
    def __init__(self, **kwargs):
        self.userid: int = kwargs.get("userid")
        self.time: datetime.datetime = datetime.datetime.fromtimestamp(kwargs.get("time"))

    def __repr__(self):
        return f"<{self.__class__.__name__} userid={self.userid} time={self.time}>"

class Votes:
    def __init__(self, **kwargs):
        self.monthly: int = kwargs.get("monthly")
        self.total: int = kwargs.get("total")
        self.votes: typing.List[Vote] = [Vote(**vote) for vote in kwargs.get("votes")]

    def __repr__(self):
        return f"<{self.__class__.__name__} monthly={self.monthly} total={self.total} votes={self.votes}>"