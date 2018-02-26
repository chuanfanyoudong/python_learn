import pandas as pd
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
if __name__=='__main__':
    iris = datasets.load_iris()
    parameters = {'C': [1, 2, 4]}
    svr = svm.SVC()
    #a = GridSearchCV.get_params()
    clf = GridSearchCV(svr, parameters, n_jobs=-1, verbose=1)
    clf.fit(iris.data, iris.target)
    best_parameters = clf.best_estimator_.get_params()
    #with open('cv_result.csv', 'w') as f:
    #    cv_result.to_csv(f)
    print('The parameters of the best model are: ')
    print(clf.best_params_)

    y_pred = clf.predict(iris.data)
    print(classification_report(y_true=iris.target, y_pred=y_pred))