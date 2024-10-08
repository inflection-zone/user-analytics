from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):

    # App
    ENVIRONMENT: str = "development"
    SERVICE_NAME="User-Analytics-Service"
    BASE_URL: str = "http://localhost:23456"
    USER_ACCESS_TOKEN_SECRET="secret"
    CIPHER_SALT="salt"
    SERVICE_IDENTIFIER=f"{SERVICE_NAME}-{ENVIRONMENT}"

    #Database
    DB_USER_NAME: str = "dbuser"
    DB_USER_PASSWORD: str = "dbpassword"
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "user_analytics"
    DB_POOL_SIZE: int = 10
    DB_POOL_RECYCLE: int = 1800
    DB_POOL_TIMEOUT: int = 30
    DB_DIALECT: str = "mysql"
    DB_DRIVER: str = "pymysql"
    DB_CONNECTION_STRING: str = f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER_NAME}:{DB_USER_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Open-telemetry
    TRACING_ENABLED: bool = False
    TRACING_EXPORTER_TYPE: str = 'NoExporter'
    TRACING_COLLECTOR_ENDPOINT: str ='http://localhost:4317'
    JAEGER_AGENT_HOST: str = "localhost"
    JAEGER_AGENT_PORT: int = 6831
    METRICS_ENABLED: bool = False

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
