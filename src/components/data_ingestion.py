import sys 
import os
from src.logger import logging 
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

try:
    logging.info('getting the original data file path')
    class data_path:
        def __init__(self,csv_filename='gemstones.csv'):
            self.model_data_path=os.path.join('notebooks',csv_filename)
        def filepath(self):
            return self.model_data_path
except Exception as e:
    logging.info(f'{e}')
    raise CustomException(e,sys)


try:
    logging.info('reading into the data')
    class data_ingestion:
        def __init__(self):
            orignal_data_path=data_path(csv_filename='gemstones.csv')
            data=pd.read_csv(orignal_data_path.filepath())
            self.data=data 
        def get_data(self):
            return self.data

except Exception as e:
    logging.info(f'{e}')
    raise CustomException(e,sys)
        
try:
    logging.info('splititng data into train and test and saving them in artifacts folder as well as raw data too')
    class splitting_saving_data:
        def __init__(self):
            data=data_ingestion()
            df=data.get_data()
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)
            self.train_csv_path='artifacts/train.csv'
            self.test_csv_path='artifacts/test.csv'
            self.raw_csv_path='artifacts/raw.csv'
            self.paths=[self.train_csv_path,self.test_csv_path,self.raw_csv_path]
            train_data.to_csv(self.train_csv_path)
            test_data.to_csv(self.test_csv_path)
            df.to_csv(self.raw_csv_path)
            with open('Train and Test Data Path.txt','w') as file:
                for i in self.paths:
                    file.write(f'{i.split("/")[-1]} : {i}\n')
except Exception as e:
    logging.info(f'{e}')
    raise CustomException(e,sys)


splitting_saving_data()







    



        
