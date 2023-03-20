from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import balanced_accuracy_score
from sklearn import preprocessing
import numpy as np
import pandas as pd
import pickle
df = pd.read_excel("Health Monitor Dataset.xlsx")
df2 = df.drop(['Dehydration.1','Medicine Overdose.1','Acidious.1','Cold .1','Cough.1'],axis=1)


label_encoder = preprocessing.LabelEncoder()
for i in df2.columns:
    if type(df2[i][2])==np.bool_ :
        df2[i]= label_encoder.fit_transform(df2[i])

X=df2.drop('Causes Respiratory Imbalance',axis=1)
y=df2['Causes Respiratory Imbalance']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
gnb = GaussianNB()
gnb.fit(X_train.values,y_train.values)
pickle.dump(gnb, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[0,0,1,0,1,2,103,99,147,105,71,8,0.94,7]]))