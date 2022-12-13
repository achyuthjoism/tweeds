import dataclasses
from typing import Optional


@dataclasses.dataclass
class Query:
    """
        Class used to query in twitter
    """
    username: Optional[str] = None
    search: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    json: Optional[str] = None
    limit: Optional[int] = None
    near: Optional[str] = None
    minLikes: Optional[int] = None
    csv: Optional[str] = None
    minReplies: Optional[int] = None
    minRetweets: Optional[int] = None
    silent: bool = False
    verified: bool = False
    geoCode: Optional[str] = None
    links: bool = False
    videos: bool = False
    images: bool = False
    media: bool = False
    year: Optional[int] = None
    today: bool = False

    def __init__(self) -> None:
        pass
