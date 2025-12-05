import pandas as pd
import statsmodels.formula.api as smf

data = {
    'Salary': [40000, 50000, 60000, 45000, 55000, 65000, 48000, 58000, 70000, 62000],
    'Education': ['High School', "Bachelor's", "Master's", 'High School',
                  "Bachelor's", "Master's", 'High School', "Bachelor's", "Master's", "Bachelor's"],
    'Experience': [2, 5, 7, 3, 6, 8, 4, 5, 9, 6]
}

df = pd.DataFrame(data)

model = smf.ols('Salary ~ Experience + C(Education, Treatment(reference="High School"))', data=df).fit()

print(model.summary())

