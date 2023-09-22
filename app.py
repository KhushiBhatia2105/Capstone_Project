from flask import Flask, render_template,request
import pickle
import numpy as np


logmodel =pickle.load(open('customerchurnpredict.pkl','rb'))


app = Flask(__name__)
 
@app.route('/')
def login():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = logmodel.predict(final_features)
    print(prediction)
    output = round(prediction[0], 2)
    if output==0:
        return render_template('index.html', prediction_text='Customer will not churn')
    else:
        return render_template('index.html', prediction_text='Customer will churn')
    



if __name__ == '__main__':
   app.run(debug=True)