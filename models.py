from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base

follow = Table(
    "follow",
    Base.metadata,
    Column("follower", Integer, ForeignKey("Users.id"), primary_key=True),
    Column("followee", Integer, ForeignKey("Users.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, nullable=False)
    gender = Column(String)
    password = Column(String, nullable=False)

    followers = relationship(
        "User",
        secondary=follow,
        primaryjoin=id == follow.c.followee,
        secondaryjoin=id == follow.c.follower,
    )

    following = relationship(
        "User",
        secondary=follow,
        primaryjoin=id == follow.c.follower,
        secondaryjoin=id == follow.c.followee,
    )
