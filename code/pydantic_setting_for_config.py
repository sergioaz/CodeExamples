from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = "../.env"

settings = Settings()
print(settings.app_name)
print(settings.debug)
print(settings.database_url)