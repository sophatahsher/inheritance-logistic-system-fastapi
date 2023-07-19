from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DRIVER: str = "postgres"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "admin"
    POSTGRES_DB: str = "fastapi_graphql"
    POSTGRES_PORT: int = 5432
    API_KEY="key88"
    APP_MAX="88"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()