import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

def outlier_present(col):
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3-q1
    lb = q1-(iqr*1.5)
    ub = q3+(iqr*1.5)
    outlier_above_ub = np.where(col>ub,1,0)
    outlier_below_lb = np.where(col<lb,1,0)
    total_outlier = outlier_above_ub.sum() + outlier_below_lb.sum()
    percentage_of_outliers = total_outlier / col.size * 100
    is_outlier = True if total_outlier>0 else False
    return (is_outlier,f"{percentage_of_outliers:.2f}%")

def find_outliers(df):
    numeric_cloumns = df.select_dtypes(include=np.number).columns
    # sns.set_theme(style="darkgrid")
    for i in numeric_cloumns:
        print(i," - ",outlier_present(df[i])[1])
        plt.figure(figsize=(8,0.5))
        sns.boxplot(x=df[i])
        plt.show()