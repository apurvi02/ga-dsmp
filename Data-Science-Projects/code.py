# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
df=pd.read_csv(path)
bank=pd.DataFrame(data=df)
categorical_var=bank.select_dtypes(include = "object")
numerical_var=bank.select_dtypes(include = "number")
print(categorical_var)
print(numerical_var)

# code ends here


# --------------
# code starts here
banks=bank.drop("Loan_ID",axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode()
banks=banks.replace(to_replace=np.nan, value=bank_mode)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here

avg_loan_amount=banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values="LoanAmount",aggfunc=np.mean)
print(avg_loan_amount)

# code ends here



# --------------
# code starts here
loan_approved_se=banks[(banks["Self_Employed"] == "Yes") & (banks["Loan_Status"] == "Y")].count()
loan_approved_nse=banks[(banks["Self_Employed"] == "No") & 
(banks["Loan_Status"] == "Y")].count()
percentage_se=loan_approved_se[0]*100/(banks["Loan_Status"].count())
percentage_nse=loan_approved_nse[0]*100/(banks["Loan_Status"].count())
print(percentage_nse)
# code ends here


# --------------
# code starts here
def m_to_y(month):
    no_of_years=month/12
    return no_of_years
loan_term=banks["Loan_Amount_Term"].apply(lambda x:m_to_y(x))
big_loan_term=banks[loan_term>=25].count()[0]
print(big_loan_term)

# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby("Loan_Status")
loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()



# code ends here


