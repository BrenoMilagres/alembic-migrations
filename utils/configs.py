from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

from os import environ

DB_USER = environ.get('DB_USER')
DB_PASS = environ.get('DB_PASS')
DB_HOST = environ.get('DB_HOST')
DB_PORT  = environ.get('DB_PORT')
DB_NAME = environ.get('DB_NAME')




class Settings(BaseSettings):
    DB_URL: str = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings: Settings = Settings()