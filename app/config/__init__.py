"""
Module contains standardized config loader and management.
This is implemented using Pydantic for type safety and docker secerts support.
"""
from pydantic import BaseSettings
from .app import AppConfig


class Config(BaseSettings):
    """
    Top-level container for holding all configs
    """
    App = AppConfig()