from dataforge.config.settings import Config
from dataforge.logging.logger import get_logger
from dataforge.ingestion.pipeline import IngestionPipeline


def main():

    config = Config()

    logger = get_logger()

    logger.info("=" * 50)
    logger.info(config.app_name)
    logger.info(f"Version: {config.app_version}")
    logger.info(f"Environment: {config.environment}")
    logger.info("=" * 50)

    pipeline = IngestionPipeline()
    pipeline.run()


if __name__ == "__main__":
    main()