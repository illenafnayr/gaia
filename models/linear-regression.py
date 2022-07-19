import pandas as pd;

iris = pd.read_csv("data/iris.csv");
print(iris.head(10));

petalWidth_petalLength = iris[["petal.width", "petal.length"]];
print(petalWidth_petalLength.head(10));

# y = mx + b
n = len(petalWidth_petalLength);
sumOfX = 0;
sumOfX2 = 0;
sumOfY = 0;
sumOfY2 = 0;
sumOfXY = 0;

for i, row in petalWidth_petalLength.iterrows():
    x_train = row['petal.length'];
    sumOfX += x_train;
    sumOfX2 += (x_train * x_train);
    y_train = row['petal.width'];
    sumOfY += y_train;
    sumOfY2 += (y_train * y_train);
    sumOfXY += (x_train * y_train);

m = ((n * (sumOfXY)) - (sumOfX * sumOfY))/((n * (sumOfX2)) - (sumOfX * sumOfX));
b = (sumOfY - (m * (sumOfX)))/n;

print("Slope: ", m);
print("Y-intercept: ", b);

input = input('Predict Y given X: ');

def linearRegression(X):
    Y = ((m * X) + b);
    print("y equals: ", Y);

linearRegression(int(input));