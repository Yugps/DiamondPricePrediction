from flask import Flask,render_template,request
import sys 
from src.logger import logging 
from src.exception import CustomException
from src.pipelines.prediction_pipeline import prediction_maker

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/prediction_making',methods=['POST','GET'])
def predict_datapoint():
    result=''
    if request.method=='POST':
        carat=float(request.form.get('carat'))
        depth=float(request.form.get('depth'))
        table=float(request.form.get('table'))
        x=float(request.form.get('x'))
        y=float(request.form.get('y'))
        z=float(request.form.get('z'))
        cut=str(request.form.get('cut'))
        color=str(request.form.get('color'))
        clarity=str(request.form.get('clarity'))
        input_params=[carat,cut,color,clarity,depth,table,x,y,z]
        pred_obj=prediction_maker(model_path='artifacts/xgbr.pkl',preprocessor_path='artifacts/preprocessor.pkl')
        result=pred_obj.data_manager(input_params)
    try:    
        return render_template('form.html',final_result=f'Price of the diamond is {result}')
    except:
        return render_template('form.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug='on')










