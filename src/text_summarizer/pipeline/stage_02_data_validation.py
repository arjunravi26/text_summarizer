from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.component.data_validation import DataValiadtion



class DataValidationPipeline:
    def __init__(self) -> None:
        pass
    
    def start(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
    