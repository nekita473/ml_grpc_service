import pandas as pd
import pickle
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X,y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0,
                               n_classes=2, n_clusters_per_class=2, flip_y=0.1, weights=None,
                                 class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, shuffle
=True, random_state=42, return_X_y=True)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, stratify=y)

df_train = pd.DataFrame(columns=['feature1', 'feature2'])
df_train.iloc[:, 0] = X_train[:, 0]
df_train.iloc[:, 1] = X_train[:, 1]

model = LogisticRegression()
model.fit(df_train, y_train)

df_val = pd.DataFrame(columns=['feature1', 'feature2'])
df_val.iloc[:, 0] = X_val[:, 0]
df_val.iloc[:, 1] = X_val[:, 1]

preds = model.predict(df_val)
print(accuracy_score(y_val, preds))

with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)