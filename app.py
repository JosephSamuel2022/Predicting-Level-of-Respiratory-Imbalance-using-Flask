from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
     
    return render_template('index.html', prediction_text='The patient has {} Respiratory Imbalance '.format(prediction))

if __name__ == '__main__':
    from waitress import serve
    serve(app,host="0.0.0.0",port=5000)
    
