import pydantic


class AppConfigSchema(pydantic.BaseSettings):
    # Uncomment this to get a required setting:
    # REQUIRED_SETTING: int

    OPTIONAL_SETTING: int = 123
