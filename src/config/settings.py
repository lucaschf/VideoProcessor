from pydantic_settings import BaseSettings


class EnvSettings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET_NAME: str


settings = EnvSettings(_env_filename='.env')
