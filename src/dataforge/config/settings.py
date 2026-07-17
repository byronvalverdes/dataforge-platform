from dotenv import load_dotenv
import os


class Config:
    """
    Central configuration class for DataForge Platform.
    Loads application settings from the .env file.
    """

    def __init__(self):
        load_dotenv()

        self.app_name = os.getenv("APP_NAME")
        self.app_version = os.getenv("APP_VERSION")
        self.environment = os.getenv("ENVIRONMENT")
        self.log_level = os.getenv("LOG_LEVEL")