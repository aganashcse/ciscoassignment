'''
This code creates unique fake objects using faker module and updates the existing db.
Argument of integer needs to be passed while executing this module which denotes the number of records needs to be created.
'''


import numpy as np
from faker import Faker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sys

faker = Faker()
DB_PATH = "C://sqlite//databases//router.db"

engine = create_engine('sqlite:///'+DB_PATH, echo=True)
meta = MetaData()
router_types = ['AG1', 'CSS']

routers = Table(
    'routers', meta,
    Column('loopback', String, primary_key=True),
    Column('hostname', String),
    Column('routertype', String),
)
meta.create_all(engine)
conn = engine.connect()
for _ in range(int(sys.argv[1])):
    ins = routers.insert().values(loopback=faker.ipv4(), hostname=faker.hostname(),
                                  routertype=np.random.choice(router_types))
    result = conn.execute(ins)

print("Sample data successfully generated and stored in DB!")

# Below code will be useful to see all table entries
# s = routers.select()
# result = conn.execute(s)
# for row in result:
#     print(row)

# print("Sample data stored are shown above!")

conn.close()
