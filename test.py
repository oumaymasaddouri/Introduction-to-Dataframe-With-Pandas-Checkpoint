"""
Write a Pandas program to create and display a DataFrame from the following dictionary data which has index labels.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas', "Elias", 'Myriam'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan , 8, 19, 20, 16],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, np.nan ,1, 3, 2],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no',np.nan , 'yes', 'yes', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
"""

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia',
                      'Dima',
                      'Katherine',
                      'James',
                      'Emily',
                      'Michael',
                      'Matthew',
                      'Laura',
                      'Kevin',
                      'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, labels)
print(df)




"""
1/Print the three first rows using head() method
"""

import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia',
                      'Dima',
                      'Katherine',
                      'James',
                      'Emily',
                      'Michael',
                      'Matthew',
                      'Laura',
                      'Kevin',
                      'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, labels)
df1 = df.head(3)
print(df.iloc[:3])
print(df.loc[:'c'])


"""
2/Extract the 'name' and 'score' columns from the DataFrame.
"""
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia',
                      'Dima',
                      'Katherine',
                      'James',
                      'Emily',
                      'Michael',
                      'Matthew',
                      'Laura',
                      'Kevin',
                      'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, labels)
print(df[['name','score']])


""" 3/Write a Pandas program to delete the 'attempts' column from the DataFrame.
"""
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia',
                      'Dima',
                      'Katherine',
                      'James',
                      'Emily',
                      'Michael',
                      'Matthew',
                      'Laura',
                      'Kevin',
                      'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df= pd.DataFrame(exam_data, labels)
df.drop(columns='attempts', inplace=True)
print(df)



"""
4/Add a new column "Success" : if the score is higher than 10 we will have 1 else we will have 0
"""
import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia',
                      'Dima',
                      'Katherine',
                      'James',
                      'Emily',
                      'Michael',
                      'Matthew',
                      'Laura',
                      'Kevin',
                      'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
df['Success']='1'
df.loc[(df['score'] > 10) , 'Success'] = 1 
df.loc[(df['score'] <= 10) , 'Success'] = 0  
df.loc[(df['score'].isnull()), 'Success'] = np.nan
print (df)

df.to_csv('out.csv')
"""5/After executing the final dataframe, export it into csv file named "my_data" """

df.to_csv('my_data.csv', index = False, encoding='utf-8') # False: not include index
print(df)