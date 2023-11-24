# This file will be responsible for doing the predictions on the data recieved through web using flask 
import sys 
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
import numpy as np
import pickle 
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
import xgboost


class prediction_maker:
    def __init__(self,model_path,preprocessor_path):
        try:
            self.model_path=model_path
            self.preprocessor_path=preprocessor_path
            self.model=pickle.load(open(self.model_path,'rb'))
            self.preprocessor=pickle.load(open(self.preprocessor_path,'rb'))
        except Exception as e:
            logging.info('error occured in loading preprocessor and model file')
            raise CustomException(e,sys)

    

    def data_manager(self,input_data):
        try:
            input_df=pd.DataFrame(input_data).T
            input_df.columns=['carat','cut'	,'color','clarity','depth','table','x','y','z']
            transformed_df=self.preprocessor.transform(input_df)
            pred=self.model.predict(transformed_df)
            return pred[0]
        except Exception as e:
            logging.info("error occured in transformation of new data and it's prediction")
            raise CustomException(e,sys)
        
    
                




