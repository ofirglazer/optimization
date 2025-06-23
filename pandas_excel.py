import pandas as pd

dataMarks = pd.read_excel('data.xlsx', sheet_name='marks')
dataPeople = pd.read_excel('data.xlsx', sheet_name='people')
print(dataMarks)
print(dataPeople)

dataAll = dataMarks.set_index('name').join(dataPeople.set_index('name'))
print(dataAll)

marks = dataAll.groupby('name').mark.mean()
print(marks)
marks.to_excel('output.xlsx')

print(dataAll.groupby('name').mark.max())
print(dataAll.groupby('name').mean())  # averaging all columns

pass
