import pandas as pd
import chardet
import json
import mysql.connector

db_conection = mysql.connector.connect(
    host = 'db',
    user = 'root',
    password = 'root',
    database = 'WEI'
)

def create_sql_file(path_to_file):
    temp_file = open(path_to_file, 'r')
    file_data = temp_file.read()
    temp_file.close()
    return file_data

def sql_to_json(table, file_name):
    new_cursor = db_conection.cursor(dictionary = True)
    new_cursor.execute(f'SELECT * FROM {table}')
    rows = new_cursor.fetchall()
    with open(f'/app/{file_name}', 'w') as json_file:
        json_file.write(json.dumps(rows, indent = 4))

new_cursor = db_conection.cursor()
new_cursor.execute('USE WEI;')

sql_to_json('WEI_TABLE', 'wei_table.json')
sql_to_json('SDGR', 'sdgr.json')
sql_to_json('COUNTRY', 'country.json')
sql_to_json('WEI_2022', 'wei_2022.json')
sql_to_json('WEG_2022', 'weg_2022.json')
sql_to_json('GGPI_2022', 'ggpi_2022.json')
sql_to_json('GPG_2022', 'gpg_2022.json')
sql_to_json('HDG_2021', 'hdg_2021.json')
sql_to_json('INDICATIONS', 'indications.json')
    

# Set filename and columns names
filename = '/app/Dataset/women_empowerment_index_treated.csv'
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
file = open('/app/Dataset/DataFrame.txt', 'w')
for tuple in data_list:
    file.write(str(tuple) + ',' + '\n')
file.close()