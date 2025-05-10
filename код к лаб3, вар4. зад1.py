
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

telo = load_breast_cancer()
x = telo.data[:, 0]
y = telo.data[:, 1]
clas = telo.target

plt.scatter(x, y, c=clas, cmap='coolwarm', s=8 )
plt.xlabel('mean radius')
plt.ylabel('mean texture')
plt.title('breast cancer')

plt.show()