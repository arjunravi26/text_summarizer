from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.component.model_trainer import ModelTrainer



class ModelTrainigPipeline:
    def __init__(self) -> None:
        pass
    def start(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
