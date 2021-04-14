# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder




#Loading the data
data=pd.read_csv(path)

# Histogram of Rating column

data.Rating.hist()
plt.show()

data=data[data['Rating']<=5]

# Histogram of Rating column

data.Rating.hist()
plt.show()

data.isnull().sum()
data.dropna(inplace=True)
total_null = data.isnull().sum()
print(total_null)
#Category vs Rating

#Setting the figure size
plt.figure()

#Plotting boxplot between Rating and Category
cat = sns.catplot(x="Category",y="Rating",data=data,kind='box',height=10)

#Rotating the xlabel rotation
cat.set_xticklabels(rotation=90)

#Setting the title of the plot
plt.title("Rating vs Category",size=20)

#Splitting the column to include only the first genre of each app
data['Genres'] = data['Genres'].str.split(';').str[0]

#Grouping Genres and Rating
gr_mean = data[['Genres','Rating']].groupby(['Genres'], as_index=False).mean() 
print(gr_mean.describe())

#Sorting the grouped dataframe by Rating
gr_mean_short = gr_mean.sort_values('Rating')
print(gr_mean_short.min(),' \n',gr_mean_short.max())

# Rating vs Installs
#Removing `,` from the column
data['Installs'] = data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs'] = data['Installs'].str.replace('+','')

#Converting the column to 'int' datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le_en = LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs'] = le_en.fit_transform(data['Installs'])

#Setting figure size

plt.figure(figsize = (10,6))

#Plotting Regression plot between Rating and Installs
sns.regplot(x='Installs',y='Rating',color='teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installment[RegPlot]',size=20)
#Code starts here

# Ratings vs Price
#Removing the dollar sign from the column

data['Price'] = data['Price'].str.replace('$','')

#Converting the column to float
data['Price'] = data['Price'].astype(float)

#Setting the figure size
plt.figure(figsize = (10,6))

#Plotting Regression plot between Rating and Price
sns.regplot(x="Price",y="Rating",data=data)

#Setting the plot title
plt.title('Rating vs Price[Reg Plot]',size = 20)

data['Last Updated']=  pd.to_datetime(data['Last Updated'], format='%B %d, %Y' )

#Setting the figure size

#plt.figure()
#data.plot.scatter(x='Last Updated',y='Rating')
#plt.show()








