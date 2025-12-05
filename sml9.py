import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = {
    'Price': [200000, 250000, 300000, 320000, 350000, 400000, 420000, 450000, 500000, 550000],
    'SqFt': [1500, 1600, 1800, 1900, 2000, 2100, 2200, 2400, 2600, 2800]
}

df = pd.DataFrame(data)

df['sqft_knot'] = np.maximum(0, df['SqFt'] - 2000)

X = sm.add_constant(df[['SqFt', 'sqft_knot']])
y = df['Price']

model = sm.OLS(y, X).fit()

print(model.summary())

plt.scatter(df['SqFt'], df['Price'], label='Data')
plt.plot(df['SqFt'], model.predict(X), label='Spline Fit')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.title('Spline Regression of Price on Square Footage')
plt.legend()
plt.show()

