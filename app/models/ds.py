from sqlalchemy import Integer, String, Column
from utils.configs import settings


class DsModel(settings.DBBaseModel):
    __tablename__ = 'ds'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    seniority = Column(String(256), nullable=False)
    cloud = Column(String(256), nullable=False)
    