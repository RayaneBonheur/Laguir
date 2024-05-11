import pandas as pd
import chardet

# Set filename and columns names
filename = 'Laguir\Dataset\women_empowerment_index_treated.csv'
names = [
    'Country', 
    'WEI_2022', 
    'WEG_2022', 
    'GGPI_2022', 
    'GPG_2022', 
    'HDG_2022', 
    'SDGR'
]

# Discover the encoding in which the .csv was saved
with open(filename, 'rb') as f:
    encode = chardet.detect(f.read())

# Input into attribute 'data' the raw csv, skipping the two first columns that are not actual values
data = pd.read_csv(
    filename, 
    skiprows = 2,
    encoding = encode['encoding'],
    names = names, 
    sep = ';'
)

# Start the creation of the tuples and their append into an array
data_list = []

for data_tuple in range(len(data)):
    temp = tuple(data.iloc[data_tuple])
    data_list.append(temp)

# Create a .txt file to store the tuples and write into it their value
file = open('Laguir\Dataset\DataFrame.txt', 'w')
for tuple in data_list:
    file.write(str(tuple) + ',' + '\n')
file.close()