from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import LeavePOut
from sklearn.model_selection import ShuffleSplit

X, y = datasets.load_iris(return_X_y=True)

clf = DecisionTreeClassifier(random_state=42)

# k_folds = KFold(n_splits = 5)
# print(k_folds)
# scores = cross_val_score(clf, X, y, cv = k_folds)
# print("Cross Validation Scores in Kfold: ", scores)
# print("Average CV Score in Kfold: ", scores.mean())
# print("Number of CV Scores used in Average in Kfold: ", len(scores))


# sk_folds = StratifiedKFold(n_splits = 5)
# scores = cross_val_score(clf, X, y, cv = sk_folds)
# print("Cross Validation Scores in skfold: ", scores)
# print("Average CV Score in skfold: ", scores.mean())
# print("Number of CV Scores used in Average in skfold: ", len(scores))


loo = LeaveOneOut()
scores = cross_val_score(clf, X, y, cv = loo)
print("Cross Validation Scores in loo: ", scores)
print("Average CV Score in loo: ", scores.mean())
print("Number of CV Scores used in Average in loo: ", len(scores))


lpo = LeavePOut(p=2)
scores = cross_val_score(clf, X, y, cv = lpo)
print("Cross Validation Scores in lpo: ", scores)
print("Average CV Score in lpo: ", scores.mean())
print("Number of CV Scores used in Average in lpo: ", len(scores))


# ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits = 5)
# scores = cross_val_score(clf, X, y, cv = ss)
# print("Cross Validation Scores in ss: ", scores)
# print("Average CV Score in ss: ", scores.mean())
# print("Number of CV Scores used in Average in ss: ", len(scores))