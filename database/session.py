"""Database engine & session creation."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'postgresql+psycopg2://newuser:password@localhost:5432/media_records',
    echo=True
)


Session = sessionmaker(bind=engine)
session = Session()

