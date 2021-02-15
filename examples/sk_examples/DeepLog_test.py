import numpy as np
from tods.tods_skinterface.primitiveSKI.detection_algorithm.DeepLog_skinterface import DeepLogSKI
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


#prepare the data

data = np.loadtxt("./500_UCR_Anomaly_robotDOG1_10000_19280_19360.txt")

# print("shape:", data.shape)
# print("datatype of data:",data.dtype)
# print("First 5 rows:\n", data[:5])

X_train = np.expand_dims(data[:10000], axis=1)
X_test = np.expand_dims(data[10001:], axis=1)

# print("First 5 rows train:\n", X_train[:5])
# print("First 5 rows test:\n", X_test[:5])

transformer = DeepLogSKI()
transformer.fit(X_train)
prediction_labels = transformer.predict(X_test)
prediction_score = transformer.predict_score(X_test)

print("Primitive: ", transformer.primitive)
print("Prediction Labels\n", prediction_labels)
print("Prediction Score\n", prediction_score)

print('Accuracy Score: ', accuracy_score(X_test, X_train))
confusion_matrix(X_test, X_train)
print(classification_report(X_test, X_train))

precision, recall, thresholds = precision_recall_curve(X_test, X_train)

f1_scores = 2*recall*precision/(recall+precision)
print('Best threshold: ', thresholds[np.argmax(f1_scores)])
print('Best F1-Score: ', np.max(f1_scores))