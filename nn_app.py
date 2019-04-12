import numpy as np
from keras.models import load_model

model = load_model('models/input_model.h5')
knockdown = np.array([0.89806022, 1.06741549, 0.98790808, 1.26951799, 0.75705166])

print("\nOn a scale of 1-10")
att = float(input("How attractive are you? "))
sinc = float(input("How sincere are you? "))
intel = float(input("How intelligent are you? "))
fun = float(input("How fun are you? "))
amb = float(input("How ambitious are you? "))

x = np.array([att, sinc, intel, fun, amb]) - knockdown
x[x < 1] = 1

y = model.predict(x.reshape(1,5))
y = round(y[0][0], 3)

print(f"There is a {int(y*100)}% chance someone will like you.")
