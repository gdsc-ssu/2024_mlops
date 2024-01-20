from typing import List, Optional, Union
from datetime import datetime
from pydantic import Field
from pydantic_settings import BaseSettings

class DBConfig(BaseSettings):
    host : str = Field(default='127.00.0.1', env='db_host')
    port : int = Field(default=3306, env='db_port')

    class Config:
        env_file = '.env_ex'

print(DBConfig())

