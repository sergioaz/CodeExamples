"""
Example demonstrating how to use Pydantic V2 for config
The Core Idea: Treat Your Settings Like a Data Model
"""


from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"
    api_key_1: str = Field(alias="OPENAI_API_KEY")
    # secret field — hidden automatically in logs/prints
    api_key_2: SecretStr = Field(alias="OPENAI_API_KEY")

    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")


settings = Settings()
print(settings.app_name)
print(settings.debug)
print(settings.database_url)
print (f"{settings=}")
print(f"Key: {settings.api_key_1}, Secret: {settings.api_key_2}")