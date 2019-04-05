import numpy as np

# Used for in class presentation
# Because only dependency we wanted was numpy, 
#   hard coded in the knockdown, intercept and 
#   the coefficients of the model

knockdown = np.array([0.89806022, 1.06741549, 0.98790808, 1.26951799, 0.75705166])
coef = [ 0.09785641, -0.01414224,  0.00640126,  0.0572765,  -0.01495719]
intercept = -0.38909181095802525
dates = 0
print("\nOn a scale of 1-10")
att = float(input("How attractive are you? "))
sinc = float(input("How sincere are you? "))
intel = float(input("How intelligent are you? "))
fun = float(input("How fun are you? "))
amb = float(input("How ambitious are you? "))


x = np.array([att, sinc, intel, fun, amb]) - knockdown
x[x < 1] = 1

y = x @ coef + intercept   
if y > 1:
    y = 1
elif y < 0:
    y = 0

print(f"There is a {int(y*100)}% chance someone will like you.")
