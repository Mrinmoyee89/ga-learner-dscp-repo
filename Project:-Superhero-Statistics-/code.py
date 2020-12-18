# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'].replace('-', 'Agender').value_counts().plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Counts')
plt.show()

print('Combat vs Intelligence Pearson =', data.Combat.corr(data.Intelligence))
print('Combat vs Intelligence Spearman =',data.Combat.corr(data.Intelligence, method='spearman'))

print('Combat vs Strength Pearson =', data.Combat.corr(data.Strength))
print('Combat vs Strength Spearman =',data.Combat.corr(data.Strength, method='spearman'))

newdata2 = data[['Name','Total']]

n=newdata2[newdata2['Total']>data.Total.quantile(.99)]
super_best_names=[n.Name]
print('super_best_names are:\n',super_best_names)







