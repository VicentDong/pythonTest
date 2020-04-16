import pymysql
db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()

data = {
    'id':'20120001',
    'age':23,
    'name':'Bob'
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
udpate = ','.join([" {key} = %s".format(key=key) for key in data])
sql += udpate
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('Sucessful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()