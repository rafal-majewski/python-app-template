import pydantic


class AppConfig(pydantic.BaseSettings):
    # required_setting: int
    OPTIONAL_SETTING: int = 123


def main() -> None:
    print("Hello World!")
    app_config = AppConfig(_env_file=".env")
    print(app_config.OPTIONAL_SETTING)


if __name__ == "__main__":
    main()
