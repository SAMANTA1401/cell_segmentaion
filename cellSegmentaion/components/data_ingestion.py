from cellSegmentaion.entity.config_entity import DataIngestionConfig
from cellSegmentaion.exception import AppException
import sys
import os
import logging
import gdown
from cellSegmentaion.logger import logging
import zipfile
from cellSegmentaion.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise logging.info(AppException(e,sys))
        
    def download_data(self)-> str:
        '''
        Fetch data from the url
        '''
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir

            os.makedirs(zip_download_dir,exist_ok=True)

            zip_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, zip_file_name)

            logging.info(f"Downloading data from {dataset_url} into {zip_file_path}")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="

            gdown.download(prefix+file_id,zip_file_path)

            logging.info(f"Data download completed")

            return zip_file_path
        

        except Exception as e:
            raise logging.info(AppException(e,sys))

    
    def extract_zip_file(self,zip_file_path:str)->str:
        """
        zip_file_path:str
        extract the zip file into the data directory
        function returns none 
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path

            os.makedirs(feature_store_path, exist_ok=True)

            with zipfile.ZipFile(zip_file_path,'r') as zip_ref:
                zip_ref.extractall(feature_store_path)

            logging.info(f"Zip file extracted")

            return feature_store_path
        
        except Exception as e:
            raise logging.info(AppException(e, sys))

    def initiate_data_ingestion(self)->str:
        logging.info("Entered initiate data ingestion method of data ingestion class")
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(   #embed two return path strings in a single class
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info("Exited initiate_data_ingestion method of data_ingestion_class")
            logging.info(f"Data ingestion artifact:{data_ingestion_artifact}")

            return data_ingestion_artifact
        
        except Exception as e:
            raise logging.info(AppException(e, sys))


# python cellSegmentaion\components\data_ingestion.py
# python -m cellSegmentaion.components.data_ingestion
if __name__=="__main__":
    ing_obj = DataIngestion()
    # zip_file_path=ing_obj.download_data()
    # ing_obj.extract_zip_file(zip_file_path)
    ing_obj.initiate_data_ingestion()
