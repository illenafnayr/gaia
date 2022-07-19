import pandas as pd;

iris = pd.read_csv("data/iris.csv");
print(iris.head(10));

petalWidth_petalLength = iris[["petal.width", "petal.length"]];
print(petalWidth_petalLength.head(10));



# y = mx + b
x = petalWidth_petalLength["petal.length"];
y = petalWidth_petalLength["petal.width"];
n = len(petalWidth_petalLength);

sumOfX = 0;
sumOfX2 = 0;
sumOfY = 0;
sumOfY2 = 0;
sumOfXY = 0;


for i, row in petalWidth_petalLength.iterrows():
    print("length: ", row['petal.length']);
    x = row['petal.length'];
    sumOfX += x;
    sumOfX2 += (x * x);

    print("width: ", row['petal.width']);
    y = row['petal.width'];
    sumOfY += y;
    sumOfY2 += (y * y);

    sumOfXY += (x * y);

m = ((n * (sumOfXY)) - (sumOfX * sumOfY))/((n * (sumOfX2)) - (sumOfX * sumOfX));
b = (sumOfY - (m * (sumOfX)))/n;

print("x: ", x);
print("y: ", y);
print("sumOfX: ", sumOfX);
print("sumOfX2: ", sumOfX2);
print("sumOfY: ", sumOfY);
print("sumOfY2: ", sumOfY2);
print("sumOfXY: ", sumOfXY);
print("m: ", m);
print("b: ", b);

input = input('Predict Y given X');

def linearRegression(X):
    Y = ((m * X) + b);
    print("y equals: ", Y);

linearRegression(int(input));