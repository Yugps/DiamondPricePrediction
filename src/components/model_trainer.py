# This file is responsile for choosing the right model and training it 
import sys
from src.exception import CustomException
from src.logger import logging
from data_transformation import pipelining_transformation
import pandas as pd
import numpy as np
import pickle



class model_picker_and_trainer:
    logging.info('model data is getting picked')
    def __init__(self):
        try:
            pt_obj=pipelining_transformation()
            x_train,x_test,y_train,y_test=pt_obj.return_train_test_splits()
            self.x_train=x_train
            self.x_test=x_test
            self.y_train=y_train
            self.y_test=y_test
        except Exception as e:
             logging.info('problem in picking up the data for the model')
             raise CustomException(e,sys)

    def model_selector(self):
        logging.info('model training has started')
        try:
            from sklearn.ensemble import RandomForestRegressor
            from sklearn.linear_model import LinearRegression,Lasso,Ridge
            from sklearn.tree import DecisionTreeRegressor
            from sklearn.svm import LinearSVC
            from sklearn.ensemble import GradientBoostingRegressor
            import xgboost as xgb
            from sklearn.metrics import mean_squared_error,mean_absolute_error
            stats=[]
            scores=[]
            mae=[]
            mse=[]
            rfr=RandomForestRegressor()
            lr=LinearRegression()
            l=Lasso()
            r=Ridge()
            dtr=DecisionTreeRegressor()
            gbr=GradientBoostingRegressor()
            xgbr=xgb.XGBRegressor()

            models=[rfr,lr,l,dtr,gbr,xgbr]
            for i in models:
                i.fit(self.x_train,self.y_train)
                stats.append({f'{i}':i.score(self.x_test,self.y_test)})
                scores.append(i.score(self.x_test,self.y_test))
                mae.append({f'{i}':mean_absolute_error(y_true=self.y_test,y_pred=i.predict(self.x_test))})
                mse.append({f'{i}':mean_squared_error(y_true=self.y_test,y_pred=i.predict(self.x_test))})
            index=scores.index(max(scores))
            best_score_model={str(models[index]):scores[index]}
            # dumping the model's pickle file 
            pickle.dump(xgbr,open('artifacts/xgbr.pkl','wb'))
            # saving the stats and best score model details in a txt file
            data_to_write=[stats,mae,mse]
            filenames=['stats','Mean absolute error','Mean squared error']
            with open('Best Model.txt','w') as file:
                    file.writelines(str(best_score_model))
                    file.close()
            
            
            with open('Training_stats.txt','w') as file:
                    for i,j in zip(data_to_write,filenames):
                        file.write(f'{j}\n')
                        file.writelines(f'{i}\n')
        except Exception as e:
             logging.info('problem occured in model training part')
             raise CustomException(e,sys)

mpt=model_picker_and_trainer()
mpt.model_selector()
        
            
        
