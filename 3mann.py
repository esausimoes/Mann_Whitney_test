#library
import pandas as pd
from scipy.stats import mannwhitneyu

# pathway
arq_path = input (r"path:")
column1_of_interest = "Controle"
column2_of_interest = "Caso"

#main
def mann_whitney_test(file_path, column_name1, column_name2):
    #reading
    df = pd.read_excel(file_path)
    data1 = df[column_name1].dropna()
    data2 = df[column_name2].dropna()

    #run
    statistic, p_value = mannwhitneyu(data1, data2)

    print(f"Mann-Whitney Statistic: {statistic:.4f}")
    print(f"P-value: {p_value:.4f}")
    
mann_whitney_test(arq_path, column1_of_interest, column2_of_interest)

