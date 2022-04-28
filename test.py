# Upon importing a library that isn't included in the requirements file:
# pip freeze > requirements.txt

# Notes:
#   - Use SQL alchemy or Pymssql utils.

import os
import json
import pymysql
import pandas as pd
import fhiry.parallel as fp



# do validation and checks before insert
def validate_string(val):
    if val is not None:
        if type(val) is int:
            # for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# read JSON file which is in the next parent folder
# with open('data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json', 'r') as f:
    # json_data = pd.read_json(f, orient='index')

df = fp.process('data')
print(df.head())

# print(json_data)

# connect to MySQL
con = pymysql.connect(host='localhost', user='root', passwd='password', db='test')
cursor = con.cursor()


# Parse into SQL server
# cursor.execute("INSERT INTO testp (person,	year,	company) VALUES (%s,	%s,	%s)", (person,	year,	company))
# con.commit()
# con.close()
