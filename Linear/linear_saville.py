import numpy as np
air_velocity = np.array([30,70,110,150,180,220,260,300,350,390])
evaporation_coefficient = np.array([0.18, 0.37, 0.35, 0.78, 0.56, 0.75, 1.18, 1.36, 1.17, 1.65])
x_mean = np.mean(air_velocity)
y_mean = np.mean(evaporation_coefficient)
xy_sum = np.sum((air_velocity - x_mean) * (evaporation_coefficient - y_mean))
x_squared_sum = np.sum((air_velocity - x_mean) ** 2)
print(f"Mean of air velocity is : {x_mean}")
print(f"Mean of evaporation coeffiicient is : {y_mean}")
b1 = xy_sum / x_squared_sum
b0 = y_mean - b1 * x_mean
def predict(x):
    return b0 + b1 * x
y_predicted = predict(air_velocity)
ssr = np.sum((y_predicted - y_mean) ** 2)
sst = np.sum((evaporation_coefficient - y_mean) ** 2)
r_squared = ssr / sst
velocity_250 = 250
evaporation_250 = predict(velocity_250)

print(f"Linear Regression Coefficients: b0 = {b0}, b1 = {b1}")
print(f"R-squared Value: {r_squared}")
print(f"Evaporation Coefficient for Air Velocity = 250: {evaporation_250}")
