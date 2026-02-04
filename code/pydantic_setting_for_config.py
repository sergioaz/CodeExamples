""" Example demonstrating how to use Pydantic V2 for config"""
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"
    openai_api_key: Optional[str] = None

    model_config = ConfigDict(env_file="../.env", extra="ignore")

settings = Settings()
print(settings.app_name)
print(settings.debug)
print(settings.database_url)
print (f"{settings=}")