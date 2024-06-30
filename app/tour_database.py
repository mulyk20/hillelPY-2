from datetime import datetime

from sqlalchemy import (Column, Date, DateTime, Float, Integer, String,
                        create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker

import app.tour_config

Base = declarative_base()


class Tour(Base):
    __tablename__ = "tours"
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)
    country = Column(String(50), nullable=False)
    hotel_class = Column(String(20), nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Tour {self.id} - {self.country} ({self.start_date} to {self.end_date})>"


engine = create_engine(app.tour_config.DB_PATH, echo=app.tour_config.DEBUG)
Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)
