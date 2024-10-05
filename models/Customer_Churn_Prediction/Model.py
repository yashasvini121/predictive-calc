from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt  

df=pd.read_csv('data/Churn_Modelling.csv')

X=df.drop('Exited',axis=1)
Y=df['Exited']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

X_train.isnull().sum()
X_test.isnull().sum()

X_test.drop('RowNumber',axis=1, inplace=True)
X_train.drop('RowNumber',axis=1, inplace=True)

X_test.drop('CustomerId',axis=1, inplace=True)
X_train.drop('CustomerId',axis=1, inplace=True)

X_train_numerical=X_train.select_dtypes(exclude=["bool_","object_"])

correlation=X_train.corr().abs()
correlation_data=(correlation.where(np.triu(np.ones(correlation.shape),k=1).astype(np.bool_)).stack().sort_values(ascending=False))

X_train.hist()

X_train_cat=X_train.select_dtypes(include=["bool_","object_"])

n1=pd.melt(X_train, value_vars=sorted(X_train_cat))
n2=sns.FacetGrid(n1, col='variable', col_wrap=3,sharex=False,sharey=False)
plt.xticks(rotation='vertical')
n2=n2.map(sns.countplot, 'value')
[plt.setp(ax.get_xticklabels(),rotation=60) for ax in n2.axes.flat]
n2.fig.tight_layout()
plt.show()

X_test.drop('Surname',axis=1, inplace=True)
X_train.drop('Surname',axis=1, inplace=True)

Y_train.hist()

exited=Y_train==1
exited=Y_train[exited]


val=(exited.shape[0]/Y_train.shape[0])*100
from sklearn import preprocessing
geography_map = {'France': 0, 'Spain': 1, 'Germany': 2}
gender_map = {'Female': 0, 'Male': 1}
X_train['Gender'] = X_train['Gender'].map(gender_map)
X_train['Geography'] = X_train['Geography'].map(geography_map)

geography_map = {'France': 0, 'Spain': 1, 'Germany': 2}
gender_map = {'Female': 0, 'Male': 1}

X_test['Gender'] = X_test['Gender'].map(gender_map)
X_test['Geography'] = X_test['Geography'].map(geography_map)

scaler=preprocessing.StandardScaler()
X_train=scaler.fit_transform(X_train)

scaler=preprocessing.StandardScaler()
X_test=scaler.fit_transform(X_test)

import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
Y_train_array = Y_train.to_numpy() 

scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)

skfolds = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

#Gradient Boosting Classifier
gbc=GradientBoostingClassifier(random_state=42)
gbc.fit(X_train, Y_train)
for fold, (training, testing) in enumerate(skfolds.split(X_train, Y_train_array), 1):
    print(f"\nFold {fold}")
    print("Training set shape:", X_train[training].shape)
    print("Testing set shape:", X_train[testing].shape) 
    print("Y_train[training] shape:", Y_train_array[training].shape)
    print("Y_train[testing] shape:", Y_train_array[testing].shape)

    clone_gbc = clone(gbc)
    x1 = X_train[training]
    y1 = Y_train_array[training]
    x2 = X_train[testing]
    y2 = Y_train_array[testing]
    
    print("y1 shape:", y1.shape)
    print("y2 shape:", y2.shape)
    
    clone_gbc.fit(x1, y1)
    pred = clone_gbc.predict(x2)
    num_correct = np.sum(pred == y2)
    accuracy = num_correct / len(pred)
    print(f"Results for fold {fold}: {accuracy:.4f}")

from sklearn.model_selection import cross_val_predict
y_pred=cross_val_predict(gbc,X_train,Y_train,cv=10)
from sklearn.metrics import confusion_matrix
confusion_matrix(Y_train,y_pred)

from sklearn.metrics import precision_score, recall_score
precision=precision_score(Y_train,y_pred)
recall=recall_score(Y_train,y_pred)

print("Precision: ",precision)
print("Recall: ",recall)

y_scores=cross_val_predict(gbc,X_train,Y_train,cv=10,method="decision_function")
from sklearn.metrics import precision_recall_curve
precisions,recalls,thresholds=precision_recall_curve(Y_train,y_scores)

def plotting(precisions,recalls,thresholds):
    plt.plot(thresholds,precisions[:-1],"b--",label="Precision")
    plt.plot(thresholds,recalls[:-1],"g--",label="Recall")
    plt.xlabel("Threshold")
 
    plt.ylim([0,1])
plotting(precisions,recalls,thresholds)
plt.show()

y_new_score=(y_scores>-0.8)
print("New precision: ",precision_score(Y_train,y_new_score))
print("New Recall: ",recall_score(Y_train,y_new_score))

from sklearn.metrics import roc_curve
false,true,thresholds=roc_curve(Y_train,y_scores)
def roc(false,true,label=None):
    plt.plot(false,true)
    plt.plot([0,1],[0,1],'k--')
    plt.axis([0,1,0,1])
    plt.xlabel("FPR")
    plt.ylabel('TPR')
roc(false,true)
plt.show()

import joblib
joblib.dump(gbc, 'saved_models/Gradient_Boosting_Classifier.joblib')
joblib.dump(scaler, 'saved_models/scaler.joblib')
