import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# 데이터 로드
train = np.loadtxt(r"C:\Users\ha\Downloads\ptrain.csv", delimiter=",")
test = np.loadtxt(r"C:\Users\ha\Downloads\ptest.csv", delimiter=",")

print("train shape:", train.shape)
print("test shape:", test.shape)
print("train labels:", np.unique(train[:, -1]))
print("test labels:", np.unique(test[:, -1]))

# x, y 분리
X_train = train[:, :2]
y_train = train[:, 2]

X_test = test[:, :2]
y_test = test[:, 2]

# 퍼셉트론 학습
clf = Perceptron()
clf.fit(X_train, y_train)

# 예측 & 정확도
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)

print("train accuracy:", accuracy_score(y_train, y_pred_train))
print("test accuracy:", accuracy_score(y_test, y_pred_test))
