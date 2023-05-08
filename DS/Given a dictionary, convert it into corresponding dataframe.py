import pandas as pd
dictionary = {'name': ['Vinay', 'Kushal', 'Aman'],
 'age' : [22, 25, 24],
 'occ' : ['engineer', 'doctor', 'accountant']}
dataframe = pd.DataFrame(dictionary)
print(dataframe)