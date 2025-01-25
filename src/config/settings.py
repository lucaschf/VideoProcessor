from pydantic_settings import BaseSettings


class EnvSettings(BaseSettings):
    """Environment variables."""

    PROJECT_NAME: str = "Video Processor"

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET_NAME: str

    DB_URI: str
    """The database connection URI."""

    DB_NAME: str
    """The database name."""

    REDOC_URL: str = "/redoc"
    DOCS_URL: str = "/docs"


settings = EnvSettings(_env_file=".env")
