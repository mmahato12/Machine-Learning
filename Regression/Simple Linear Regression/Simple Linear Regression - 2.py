import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
X = dataset['YearsExperience'].values
y = dataset['Salary'].values

m=len(X)

mean_X=np.mean(X)
mean_Y=np.mean(y)

VarX=0
CovXY=0
for i in range(m):
	VarX += (mean_X-X[i])**2
	CovXY += (mean_X - X[i]) * (mean_Y - y[i])

b1 = CovXY / VarX;
b0 = mean_Y - mean_X * b1;

plt.scatter(X, y, color = 'red')
plt.plot(X, X*b1+b0, color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()