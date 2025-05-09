from dynaconf import Dynaconf

# 初始化 Dynaconf
settings = Dynaconf(
    environments=True,  # 启用多环境
    settings_files=[
        "src/config/application_development.yml",
        "src/config/application_production.yml"
    ],
    env_switcher="ENV_FOR_PROFILE",
    env="development",
    load_dotenv=True
)