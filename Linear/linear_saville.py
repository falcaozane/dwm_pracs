import numpy as np
# air velocity => x
# evaporation => y

air_velocity = np.array([30,70,110,150,180,220,260,300,350,390])
evaporation_coefficient = np.array([0.18, 0.37, 0.35, 0.78, 0.56, 0.75, 1.18, 1.36, 1.17, 1.65])

# find mean 
x_mean = np.mean(air_velocity)
y_mean = np.mean(evaporation_coefficient)

print(f"Mean of air velocity is : {x_mean}")
print(f"Mean of evaporation coeffiicient is : {y_mean}")


# velocity * coefficient
xy_sum = np.sum((air_velocity - x_mean) * (evaporation_coefficient - y_mean))

# velocity square
x_squared_sum = np.sum((air_velocity - x_mean) ** 2)

# linear regg formulae
b1 = xy_sum / x_squared_sum
b0 = y_mean - b1 * x_mean

def predict(givenAttribute):
    return b0 + b1 * givenAttribute


# residual = predicted - y_mean
# total  = actual - y_mean

y_predicted = predict(air_velocity)
ssr = np.sum((y_predicted - y_mean) ** 2)  # sum of square of residuals = predicted value - actual value
sst = np.sum((evaporation_coefficient - y_mean) ** 2) # sum of squares of total

r_squared = ssr / sst

# For given velocity= 250, predict the evaporation_coefficient.
velocity_250 = 250
evaporation_250 = predict(velocity_250)

print(f"Linear Regression Coefficients: b0 = {b0}, b1 = {b1}")
print(f"R-squared Value: {r_squared}")
print(f"Evaporation Coefficient for Air Velocity = 250: {evaporation_250}")
