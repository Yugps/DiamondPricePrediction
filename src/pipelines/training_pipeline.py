from src.components.model_trainer import model_picker_and_trainer
from src.components.data_transformation import pipelining_transformation

mpt_obj=model_picker_and_trainer()
mpt_obj.model_selector() # if you will run this file then whole training pipeline will start taking place 