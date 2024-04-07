from cellSegmentaion.entity.config_entity import ModelTrainerConfig
from cellSegmentaion.entity.artifact_entity import ModelTrainerArtifact
from cellSegmentaion.logger import logging
import os
import sys
from cellSegmentaion.exception import AppException



class ModelTrainer:
    def __init__(
            self,
            model_trainer_config: ModelTrainerConfig
    ):
        self.model_trainer_config = model_trainer_config

    
    def initiate_model_trainer(self)-> ModelTrainerArtifact: 
        logging.info("Entered the initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("unzipping data")

            # conda install git
            os.system("unzip data.zip") #his command unzips the file named data.zip in the current working directory. The os.system function is a way to run shell commands from within Python code.
            os.system("rm data.zip")  # remove zip file after unzipping

            os.system(f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data=datas.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true")
            os.makedirs(self.model_trainer_config.model_trainer_dir,exist_ok=True)

            os.system(f"cp runs/segment/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")  #copy path and  file
            
            os.system("rm -rf yolov8s-seg.pt")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="artifacts/model_trainer/best.pt"
            )
            logging.info("Exited the initiate_model_trainer method of ModelTrainer class")
            logging.info("Model trainer artifact: {}".format(model_trainer_artifact))
            logging.info("best.pt model saved")

            return model_trainer_artifact

            

        except Exception as e:
            raise logging.info(AppException(e, sys))
        
# python -m cellSegmentaion.components.model_trainer
if __name__=="__main__":
    model_trainer_config= ModelTrainerConfig()
    obj = ModelTrainer(model_trainer_config)
    obj.initiate_model_trainer()