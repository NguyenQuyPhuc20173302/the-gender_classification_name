import pandas as pd

def encode(size):
    data_male = pd.read_csv('data_male.csv')
    data_female = pd.read_csv('data_female.csv')
    label_male = []
    for i in range(len(data_male)):
        label_male.append(1)
    data_male['Label'] = label_male
    data_male = data_male[0:size]

    label_female = []
    for i in range(len(data_female)):
        label_female.append(0)
    data_female['Label'] = label_female
    data_female = data_female[0:size]
    data = data_male.append(data_female)
    data.to_csv('gender_data.csv', index=None)

