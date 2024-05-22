from text_summarizer.logging import logger
from src.text_summarizer.pipeline.stage01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.text_summarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from src.text_summarizer.pipeline.stage_03_data_transformation import (
    DataTransformationPipeline,
)
from src.text_summarizer.pipeline.stage_o4_model_training import (
    ModelTrainigPipeline,
)
from src.text_summarizer.pipeline.stage_05_model_evaluation import (
    EvaluationPipeline,
)

STAGE_NAME_01 = "DATA INGESTION STAGE"
STAGE_NAME_02 = "DATA VALIDATION STAGE"
STAGE_NAME_03 = "DATA TRANSFORMATION STAGE"
STAGE_NAME_04 = "MODEL TRAINING STAGE"
STAGE_NAME_05 = "MODEL EVALUATION STAGE"


if __name__ == "__main__":
    try:
        logger.info(f"Starting>>>> {STAGE_NAME_01}")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.start()
        logger.info(f"Completed {STAGE_NAME_01}")
        
        logger.info(f"Starting>>>> {STAGE_NAME_02}")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.start()
        logger.info(f"Completed {STAGE_NAME_02}")
        
        logger.info(f"Starting>>>> {STAGE_NAME_03}")
        data_transformation_pipeline = DataTransformationPipeline()
        data_transformation_pipeline.start()
        logger.info(f"Completed {STAGE_NAME_03}")
        
        logger.info(f"Starting>>>> {STAGE_NAME_04}")
        model_training_pipeline = ModelTrainigPipeline()
        model_training_pipeline.start()
        logger.info(f"Completed {STAGE_NAME_04}")
        
        logger.info(f"Starting>>>> {STAGE_NAME_05}")
        evaluation_pipeline = EvaluationPipeline()
        evaluation_pipeline.start()
        logger.info(f"Completed {STAGE_NAME_05}")
        

    except Exception as e:
        logger.exception(e)
        raise e
