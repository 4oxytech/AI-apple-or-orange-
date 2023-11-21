import numpy as np

def activate(x):
    return 0 if x < 0.5 else 1
def go(color, form, taste):
    x = np.array([color, form, taste])
    w1 = [0.1, 0.5, 0.2]
    w2 = [0.5, 0.5, 0.5]
    weight1 = np.array([w1, w2])
    weight2 = np.array([-1, 1])

    sum_hiden = np.dot(weight1, x)
    print('Значение сумм на нейронах скрытого слоя: ', str(sum_hiden))

    sum_out = np.array([activate(x) for x in sum_hiden])
    print('Значение сумм на выходных нейронах скрытого слоя: ', str(sum_out))

    sun_end = np.dot(weight2, sum_out)
    y = activate(sun_end)
    print("Нейросеть считает", str(y))
    return y

color = 0
form = 1
taste = 1
result = go(color, form, taste)

if result == 1:
    print("Apple")
else:
    print("Orange")

