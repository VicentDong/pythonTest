import pymysql
db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()
sql = '''
CREATE TABLE IF NOT EXISTS students (
    id VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY(id)
)'''
cursor.execute(sql)

# id = '2012001'
# user = 'Bob'
# age = 20
data = {
    'id': '2012002',
    'name' : 'Peter',
    'age' : 22
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data)) 
sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        print('successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
