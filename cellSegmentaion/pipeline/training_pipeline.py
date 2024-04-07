from cellSegmentaion.entity.config_entity import DataIngestionConfig, DataValidationConfig, ModelTrainerConfig
from cellSegmentaion.logger import logging
from cellSegmentaion.entity.artifact_entity import DataIngestionArtifact,ModelTrainerArtifact
from cellSegmentaion.components.data_ingestion import DataIngestion
from cellSegmentaion.components.data_validation import DataValidation
from cellSegmentaion.components.model_trainer import ModelTrainer
import sys
from cellSegmentaion.exception import AppException



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("getting the data from the url")

            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("got the data from the url")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifact

        except Exception as e:
            raise logging.info(AppException(e, sys))
        

    def start_data_validation(
            self,data_ingestion_artifact:DataIngestionArtifact
            )->DataIngestionArtifact:
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingesion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifact

        except Exception as e:
            raise logging.info(AppException(e, sys))


    def start_model_trainer(self)->ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()

            return model_trainer_artifact
        
        except Exception as e:
            raise logging.info(AppException(e, sys))

        

    


    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
                )
            
            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
            else:
                raise Exception("Data Validation Failed")



        except Exception as e:
            raise logging.info(AppException(e, sys))
        
        
        
# python -m cellSegmentaion.pipeline.training_pipeline
if __name__=="__main__":
    obj = TrainPipeline()
    obj.run_pipeline()
