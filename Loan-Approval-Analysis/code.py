# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

                    ##Step 1

bank=pd.DataFrame(bank_data)
print(bank)

categorical_var=bank.select_dtypes(include = 'object')
print('categorical_var=' , categorical_var )
print(categorical_var.shape)

numerical_var=bank.select_dtypes(include = 'number')
print('numerical_var=' , numerical_var)
print(numerical_var.shape)

                    ##Step 2

banks=bank.drop(columns=['Loan_ID'])
print(banks)

isnull=banks.isnull().sum()
print(isnull)

bank_mode=banks.mode().iloc[0]
print('bank_mode=' , bank_mode)

banks=banks.fillna(bank_mode)
print('banks:' , banks)
print('bank.shape=' , banks.shape)
print('banks.isnull().sum().values.sum()=' , banks.isnull().sum().values.sum())

                    ##Step 3

avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'] ,aggfunc=np.mean)
print('avg_loan_amount=' , avg_loan_amount)
print('avg_loan_amount=' , avg_loan_amount['LoanAmount'][1])

                    ##Step 4

loan_approved_se=banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')][['LoanAmount']].count()
print('loan_approved_se=' , loan_approved_se)

loan_approved_nse=banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')][['LoanAmount']].count()
print('loan_approved_nse=' , loan_approved_nse)

print('banks_Loan_Status_count=' , banks['Loan_Status'].count())

percentage_se=(loan_approved_se/614)*100
print('percentage_se=' , percentage_se)

percentage_nse=(loan_approved_nse/614)*100
print('percentage_nse=' , percentage_nse)

                    ##Step 5

loan_term=banks.Loan_Amount_Term.apply(lambda x: x/12)
print('loan_term=' , loan_term)

big_loan_term=loan_term[loan_term>=25].count()
print('big_loan_term=' , big_loan_term)

                    ##Step 6

loan_groupby=banks.groupby(['Loan_Status'])[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()
print('mean_values=' , mean_values)
print('mean_values_iloc', mean_values.iloc[1,0])

#Code starts here




