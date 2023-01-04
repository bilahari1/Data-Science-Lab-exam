from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

irisData = load_iris()
a = irisData.data
b = irisData.target

a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.3, random_state=42)
model = GaussianNB()
model.fit(a_train, b_train)

c = model.predict(a_test)
acc = accuracy_score(b_test, c)
print(c)
print('Accuracy : ', acc)
plt.plot(a_test, b_test)
plt.show()
