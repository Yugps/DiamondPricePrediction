# In this file all kind of data transformation takes place 
from src.components.data_ingestion import splitting_saving_data
from src.logger import logging 
from src.exception import CustomException
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
import pandas as pd 
import numpy as np
import pickle 
import sys


class data_preparation:
    def __init__(self):
        logging.info('data_preparation has started')
        try:
            ssd=splitting_saving_data()
            train_path,test_path=ssd.return_paths()
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            complete_df=pd.concat([train_df,test_df],axis='rows')
            complete_df.to_csv('artifacts/complete_df.csv')
            complete_df.drop('id',axis='columns',inplace=True)
            obj_columns=[]
            numerical_columns=[]
            for c in complete_df.columns:
                if complete_df[f'{c}'].dtype==object:
                    obj_columns.append(c)
                else:
                    numerical_columns.append(c)
            numerical_columns.remove('price')
            self.numerical_columns=numerical_columns
            self.obj_columns=obj_columns
            self.complete_df=complete_df
            print(self.numerical_columns)
            print(self.obj_columns)
            print(complete_df.columns)
        except Exception as e:
            logging.info('exception occured in data preparation under data transformation')
            raise CustomException(e,sys)

    def return_column_names_df(self):
        return self.obj_columns,self.numerical_columns,self.complete_df


class pipelining_transformation:
    def __init__(self):
        logging.info('pipelining the transformation has initiated')
        try:
            data_preparation_obj=data_preparation()
            obj_columns,numerical_columns,complete_df=data_preparation_obj.return_column_names_df()
            
            # For categorical columns
            cat_pipeline=Pipeline(steps=[('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',OrdinalEncoder()),
                    ('scaler',StandardScaler())])
            
            # For numerical columns
            numeric_pipeline=Pipeline(steps=[('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())])
            
            # applying column transformer over pipelines
            ct=ColumnTransformer([('cat_pipeline',cat_pipeline,obj_columns),
                        ('numeric_pipeline',numeric_pipeline,numerical_columns)])
            
            # data transformation by pushing data through pipelines
            transformed_data=ct.fit_transform(complete_df)
            self.preprocessor=ct
            
            # Dividing data into x and y variables
            x=pd.DataFrame(transformed_data,columns=ct.get_feature_names_out())
            y=complete_df['price']

            # train and test slitting the data 
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
            self.x_train=x_train
            self.x_train.to_csv('artifacts/x_train.csv')
            self.x_test=x_test
            self.x_test.to_csv('artifacts/x_test.csv')
            self.y_train=y_train
            self.y_train.to_csv('artifacts/y_train.csv')
            self.y_test=y_test
            self.y_test.to_csv('artifacts/y_test.csv')
        except Exception as e:
            logging.info('problem occured in pipelining transformation under data transformation')
            raise CustomException(e,sys)    

    def return_train_test_splits(self):
        logging.info('saving preprocessor.pkl file in artifacts folder')
        try:
            pickle.dump(self.preprocessor,open('artifacts/preprocessor.pkl','wb'))
            return self.x_train,self.x_test,self.y_train,self.y_test
        except Exception as e:
            logging.info('problem has occured in saving the preprocessor.pkl file')
            raise CustomException(e,sys)
        


    


    
    
    





     
        
     




    


