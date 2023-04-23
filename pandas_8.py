import pandas as pd
xlsx = pd.ExcelFile('excel_1.xls')
data = pd.read_excel(xlsx,'Sheet1')
print(data)