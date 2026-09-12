import pandas as pd
from sklearn.impute import SimpleImputer

data = pd.DataFrame({
    "age":[12,18,None,27,16],
    "height":[5.2,4.8,None,6.2,5.1]
    })

data

imputer = SimpleImputer(strategy="median")

imputer.fit(data)

imputer.statistics_

imputed_data = imputer.transform(data)

newdf = pd.DataFrame(imputed_data,columns=data.columns)

newdf