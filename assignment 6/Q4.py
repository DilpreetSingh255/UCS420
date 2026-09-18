import numpy as np

# Data

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

y = np.array([40, 65, 30, 85])

# (a) Shape and dimensions

print("Shape of X:", X.shape)
print("Dimensions of X:", X.ndim)

# (b) Transpose

XT = X.T

print("\nTranspose of X:")
print(XT)

# (c) X.T @ X

XTX = XT @ X

print("\nX.T @ X:")
print(XTX)

# (d) Inverse of X.T @ X

XTX_inv = np.linalg.inv(XTX)

print("\nInverse of (X.T @ X):")
print(XTX_inv)

# (e) OLS Equation
# β = (X.T X)^-1 X.T y

beta = XTX_inv @ XT @ y

print("\nRegression Coefficients (Beta):")
print(beta)

# (f) Meaning of coefficients

print("\nInterpretation:")
print("Beta[0] -> Effect of Sleep Hours")
print("Beta[1] -> Effect of Activity Level")
print("Beta[2] -> Effect of Stress Level")

# (g) Predict score for new user

new_user = np.array([5, 40, 7])

predicted_score = new_user @ beta

print("\nPredicted Assistance Score:")
print(predicted_score)