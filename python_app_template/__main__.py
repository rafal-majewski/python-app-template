import pydantic


class AppConfig(pydantic.BaseSettings):
    # required_setting: int
    optional_setting: int = 123


def main() -> None:
    print("Hello World!")
    app_config = AppConfig(_env_file=".env")
    print(app_config.optional_setting)


if __name__ == "__main__":
    main()
