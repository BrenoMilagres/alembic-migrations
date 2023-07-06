from sqlalchemy import Integer, String, Column
from utils.configs import settings


class AeModel(settings.DBBaseModel):
    __tablename__ = 'da'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    seniority = Column(String(256), nullable=False)
    cloud = Column(String(256), nullable=False)
    code_language = Column(String(8), nullable=False)
    orchestrator = Column(Integer, nullable=False)
    