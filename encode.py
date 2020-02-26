import pandas as pd

data_male = pd.read_csv('data_male.csv', sep='\t')
data_female = pd.read_csv('data_female.csv', sep='\t')
size = 1000

label_male = []
for i in range(len(data_male)):
    label_male.append(1)
data_male['label'] = label_male
data_male = data_male[0:size]



label_female = []
for i in range(len(data_female)):
    label_female.append(0)
data_female['label'] = label_female
data_female = data_female[0:size]

data_male.append(data_female)
print(data_male)

