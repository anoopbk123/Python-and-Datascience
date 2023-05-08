import pandas as pd
sr = pd.Series(pd.date_range('2022-05-01','2022-05-12',freq = 'D'))
# To avoid dtype
# Series.to_string
print(sr.to_string(index=False))