"""
File contains APP configurations
"""
from typing import List
from pydantic import BaseSettings, Field


class AppConfig(BaseSettings):
    """
    Container for APP Configs
    """
    name: str = Field(...)
    description: str = Field(...)
    version: str = Field(...)
    authors: List[str] = Field(...)
    debug: bool = Field(...)

    class Config:
        """
        Internal configurations for the container
        """
        env_file = '.env'
        env_prefix = "APP_"
        env_file_encoding = 'utf-8'
        case_sensitive = False
