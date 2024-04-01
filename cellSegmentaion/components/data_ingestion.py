from cellSegmentaion.entity.config_entity import DataIngestionConfig
from cellSegmentaion.exception import AppException
import sys
import os
import logging
import gdown
from cellSegmentaion.logger import logging



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

        

# python cellSegmentaion\components\data_ingestion.py
# python -m cellSegmentaion.components.data_ingestion
if __name__=="__main__":
    ing_obj = DataIngestion()
    ing_obj.download_data()
