from text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_02_data_validation import DataValidationPipeline




STAGE_NAME = "DATA INGESTION STAGE"

if __name__ == '__main__':
    try:
        logger.info(f"Starting>>>> {STAGE_NAME}")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.main()
        logger.info(f"Completed {STAGE_NAME}")
        logger.info(f"Starting>>>> {STAGE_NAME}")
        data_ingestion_pipeline = DataValidationPipeline()
        data_ingestion_pipeline.start()
        logger.info(f"Completed {STAGE_NAME}")
        
    except Exception as e:
        logger.exception(e)
        raise e
