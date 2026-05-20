import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    train_path = os.path.join(base_dir, 'dataset_preprocessing', 'train.csv')
    test_path = os.path.join(base_dir, 'dataset_preprocessing', 'test.csv')
    
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    
    X_train = train.drop('Class', axis=1)
    y_train = train['Class']
    X_test = test.drop('Class', axis=1)
    y_test = test['Class']
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_data()
    
    mlflow.sklearn.autolog()
    
    with mlflow.start_run() as run:
        clf = RandomForestClassifier(random_state=42, n_estimators=10, max_depth=5)
        clf.fit(X_train, y_train)
        
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"Model trained with Accuracy: {acc:.4f}")
        
        with open("run_id.txt", "w") as f:
            f.write(run.info.run_id)
        
        mlflow.sklearn.log_model(clf, "model")
        
        # Triggering build-docker with conda env manager