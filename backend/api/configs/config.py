from pydantic import Field, MySQLDsn, RedisDsn
from typing import Type, Tuple
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

class SETTINGS(BaseSettings):
    SECRET_KEY: str = "%4fis7OqF8Ee9hI9Xc#eOHInV@1f@4V0"
    JWT_SECRET: str = "496B7D10E7E5FD934999E13FFFFF1B075EE65EE39C5C37453EC5F6EE35888143"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    GOOGLE_API_KEY: str|None = None
    SMS_SEND_ADDRESS: str|None = None
    DATABASE_URL: str
    REDIS_DATABASE_URL : str|None = None

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return  dotenv_settings, env_settings,  file_secret_settings, init_settings

TESTING = SETTINGS(
    DATABASE_URL="sqlite://"
)

Setting : SETTINGS|None = TESTING
