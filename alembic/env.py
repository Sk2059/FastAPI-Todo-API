from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Alembic config object
config = context.config

database_url = os.getenv("DATABASE_URL")

if database_url:
    database_url = database_url.replace("%", "%%")

config.set_main_option(
    "sqlalchemy.url",
    database_url
)

# Logging configuration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import metadata
from app.core.database import Base
from app.models import *

target_metadata = Base.metadata