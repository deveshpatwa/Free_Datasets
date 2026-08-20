# Install via: pip install feature-engine
from feature_engine.outliers import Winsorizer
import pandas as pd

df = pd.DataFrame({"income":[45,23,78,56,98,56,34,3500]})
print(df)

winsor = Winsorizer(capping_method="iqr",tail="both")
winsor.fit_transform(df)

winsor = Winsorizer(capping_method="quantiles",tail="both",fold=0.05)
winsor.fit_transform(df)

