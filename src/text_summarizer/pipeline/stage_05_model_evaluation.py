from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.component.model_evaluation import ModelEvaluation


class EvaluationPipeline:
    def __init__(self) -> None:
        pass 
    def start(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()
