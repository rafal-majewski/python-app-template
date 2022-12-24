from python_app_template.app_config import app_config


def main() -> None:
    print("Hello World!")
    print(app_config.OPTIONAL_SETTING)


if __name__ == "__main__":
    main()
