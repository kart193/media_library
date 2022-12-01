### models.py ###

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

engine = create_engine(
    'postgresql+psycopg2://newuser:password@localhost:5432/media_records',
    echo=True
)

Base = declarative_base()


class Medias(Base):
    __tablename__ = 'test_table'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    type = Column(String)

    def __repr__(self):
        return f"Media {self.title} of id {self.id}"


# The following is an example implementation for inheritance - in case if files of each type is
# going to be huge.

# class Music(Medias):
#     def __init__(self):
#         super().__init__()

Base.metadata.create_all(engine)

