import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import os

def load_data():
    train = pd.read_csv('dataset_preprocessing/train.csv')
    test = pd.read_csv('dataset_preprocessing/test.csv')
    
    X_train = train.drop('Class', axis=1)
    y_train = train['Class']
    X_test = test.drop('Class', axis=1)
    y_test = test['Class']
    
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = load_data()
    
    mlflow.sklearn.autolog()
    
    with mlflow.start_run(run_name='Basic_RandomForest'):
        clf = RandomForestClassifier(random_state=42, n_estimators=10)
        clf.fit(X_train, y_train)
        
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f'Model Basic berhasil dilatih dengan Accuracy: {acc:.4f}')
