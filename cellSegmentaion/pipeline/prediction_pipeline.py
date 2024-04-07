
from cellSegmentaion.entity.config_entity import ModelTrainerConfig
import ultralytics
import os,sys
from cellSegmentaion.exception import AppException
from cellSegmentaion.logger import logging
from cellSegmentaion.utils.main_util import encodeImageIntoBase64





class Prediction:
        def __init__(self):
             pass
            

        def predict(self):
            try:
                model_path=ModelTrainerConfig()
                os.system(f"yolo task=segment mode=predict model={model_path.model_trainer_dir}/best.pt  conf=0.25 source=static/inputImage.jpg save=true")
                opencodedbase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
                # # result = {"image": opencodedbase64.decode('utf-8')}

                os.system(f"cp runs/segment/predict/inputImage.jpg   static/output/")
                result = opencodedbase64.decode('utf-8')
             

                os.system("rm -rf runs")
                


            # except ValueError as val:
            #     print(val)
            #     return Response("Value not found inside  json data")
            # except KeyError:
            #     return Response("Key value error incorrect key passed")
            # except Exception as e:
            #     print(e)
            #     result = "Invalid input"

            
                # print(result)
                # logging.info(f"{result}")

                return result
            
            except Exception as e:
                 raise logging.info(AppException(e, sys))
                        
                        
                        
# python -m cellSegmentaion.pipeline.prediction_pipeline               
if __name__ == "__main__":
     obj = Prediction()
     obj.predict()