import dataclasses


@dataclasses.dataclass
class Query:
    username: str
    search: str
    since: str
    until: str
    json: str
    limit: int
    near: str
    minLikes: int
    csv: str
    minReplies: int
    minRetweets: int
    silent: str

    def __init__(self) -> None:
        pass
