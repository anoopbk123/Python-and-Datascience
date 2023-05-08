import pandas as pd
lists = [[2, 'Vishal', 22],
 [1, 'Kushal', 25],
 [1, 'Aman', 24]]
dataframe = pd.DataFrame(lists, columns = ['id', 'name', 'age'])
print(dataframe)
