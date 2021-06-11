import typing
import datetime
from dateutil import parser

class Bot:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get("name")
        self.id: int = kwargs.get("id")
        self.discriminator: int = kwargs.get("discriminator")
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
        self.added: datetime.datetime = parser.parse(kwargs.get("added"))
        self.invites: int = kwargs.get("invites")
        self.page_views: int = kwargs.get("page_views")
        self.donate_url: str = kwargs.get("donate_url")
        self.avatar_url: str = kwargs.get("avatar_url")
        self.privacy_policy_url: str = kwargs.get("privacy_policy_url")
        self.status: str = kwargs.get("status")
        self.staff: bool = kwargs.get("staff")
        self.premium: bool = kwargs.get("premium")
        self.uses_slash_commands: bool = kwargs.get("uses_slash_commands")

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} name='{self.name}' discriminator='{self.discriminator}' prefix='{self.prefix}' library='{self.library}'>"

class User:
    def __init__(self, **kwargs):
        self.id: int = kwargs.get("id")
        self.name: str = kwargs.get("name")
        self.discriminator: int = kwargs.get("discriminator")
        self.bio: str = kwargs.get("bio")
        self.staff: bool = kwargs.get("staff")
        self.administrator: bool = kwargs.get("administrator")
        self.developer: bool = kwargs.get("developer")
        self.certified_developer: bool = kwargs.get("certified_developer")
        self.joined: datetime.datetime = parser.parse(kwargs.get("joined"))
        self.reddit: str = kwargs.get("reddit")
        self.snapchat: str = kwargs.get("snapchat")
        self.instagram: str = kwargs.get("instagram")
        self.twitter: str = kwargs.get("twitter")
        self.github: str = kwargs.get("github")
        self.website: str = kwargs.get("website")
        self.avatar_url: str = kwargs.get("avatar_url")
        self.bug_hunter: bool = kwargs.get("bug_hunter")
        self.blacklisted: bool = kwargs.get("blacklisted")
        self.premium: bool = kwargs.get("premium")
        self.vanity_url: str = kwargs.get("vanity_url")
        self.last_login: datetime.datetime = parser.parse(kwargs.get("last_login"))


    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} discriminator='{self.discriminator}' bio='{self.bio}' staff={self.staff}>"

class Vote:
    def __init__(self, **kwargs):
        self.user: int = kwargs.get("user")
        self.time: datetime.datetime = parser.parse(kwargs.get("time"))

    def __repr__(self):
        return f"<{self.__class__.__name__} user={self.user} time={self.time}>"

class Votes:
    def __init__(self, **kwargs):
        self.votes: typing.List[Vote] = [Vote(**vote) for vote in kwargs.get("votes")]

    def __repr__(self):
        return f"<{self.__class__.__name__} votes={self.votes}>"

class Review:
    def __init__(self, **kwargs):
        self.feedback: str = kwargs.get("feedback")
        self.recommended: bool = kwargs.get("recommended")
        self.time: datetime.datetime = parser.parse(kwargs.get("time"))

    def __repr__(self):
        return f"<{self.__class__.__name__} feedback={self.feedback} recommended={self.recommended}>"

class Reviews:
    def __init__(self, **kwargs):
        self.reviews: typing.List[Review] = [Review(**review) for review in kwargs.get("reviews")]

    def __repr__(self):
        return f"<{self.__class__.__name__} reviews={self.reviews}>"