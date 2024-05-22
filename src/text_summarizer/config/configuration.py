from src.text_summarizer.constant import *
from src.text_summarizer.utils.common import read_yaml, create_directories
from src.text_summarizer.entity import DataIngestionConfig
from src.text_summarizer.entity import DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig


class ConfigurationManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH
    ):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config['root_dir']),
            data_path=Path(config['data_path']),
            model_ckpt=config['model_ckpt'],
            num_train_epochs=int(params['num_train_epochs']),
            warmup_steps=int(params['warmup_steps']),
            per_device_train_batch_size=int(params['per_device_train_batch_size']),
            weight_decay=float(params['weight_decay']),
            logging_steps=int(params['logging_steps']),
            evaluation_strategy=params['evaluation_strategy'],
            eval_steps=int(params['eval_steps']),
            save_steps=int(float(params['save_steps'])),
            gradient_accumulation_steps=int(params['gradient_accumulation_steps'])
        )



        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )

        return model_evaluation_config


    


                            
