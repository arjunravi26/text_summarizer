
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.component.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass
    
    def start(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
