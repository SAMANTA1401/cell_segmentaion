from cellSegmentaion.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from cellSegmentaion.entity.config_entity import DataValidationConfig
from cellSegmentaion.exception import AppException
from cellSegmentaion.logger import logging
import os, sys
import shutil




class DataValidation:
    def __init__(self,
        data_ingesion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingesion_artifact = data_ingesion_artifact
            self.data_validation_config = data_validation_config
        
        except Exception as e:
            raise logging.info(AppException(e,sys))
        
    
    def validate_all_files_exist(self) -> bool:
        validation_status = None

        all_files = os.listdir(self.data_ingesion_artifact.feature_store_path) #list of directory in feature store path of train,test,valid
        # also prsent in data_vlidation_config.required_file_list
        
                                                
        for file in all_files:
            if file not in self.data_validation_config.required_file_list:
                validation_status = False

                os.makedirs(self.data_validation_config.data_vlidation_dir,exist_ok=True)

                with open(self.data_validation_config.valid_status_file_dir,'w') as f:
                    f.write(f"Validation status: {validation_status}")

            else:
                validation_status = True
                
                os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)

                with open(self.data_validation_config.valid_status_file_dir,'w') as f:
                    f.write(f"Validation status: {validation_status}")


            logging.info(f"Validation status: {validation_status}")

        return validation_status
    


    def initiate_data_validation(self)-> DataValidationConfig:
        logging.info("Entered the data validation method or component")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifacts = DataValidationArtifact(
                validation_status=status
            )
            logging.info(f"Data validation artifact: {data_validation_artifacts}")

            if status:
                shutil.copy(self.data_ingesion_artifact.data_zip_file_path, os.getcwd()) #  working
                logging.info("data.zip copied to current directory")

            return data_validation_artifacts
        
        except Exception as e:
            raise logging.info(AppException(e, sys))
    




