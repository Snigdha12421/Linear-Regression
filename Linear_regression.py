X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

n = len(X)

sum_x = sum(X)
sum_y = sum(Y)
sum_xy = sum([X[i] * Y[i] for i in range(n)])
sum_x2 = sum([X[i] ** 2 for i in range(n)])

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n

print("Slope (m) =", m)
print("Intercept (b) =", b)

x_new = float(input("Enter x to predict y: "))
y_pred = m * x_new + b
print("Predicted y =", y_pred)
