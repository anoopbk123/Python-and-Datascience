import pandas as pd
given_list = [2, 4, 5, 6, 9]
series = pd.Series(given_list, index = [1, 3, 5, 7, 9])
print(series)