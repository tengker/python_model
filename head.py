from ppgan.apps import Photo2CartoonPredictor
import paddle
import pymysql
import sys

def head(path,account):
    paddle.set_device('gpu')
    p2c = Photo2CartoonPredictor(output_path='C:\\carton\\output')
    result=p2c.run(path)
    db = pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db='app')
    r= db.cursor()
    sql = "update carton set path='"+ 'C:/carton/output/p2c_cartoon.png' +"' where account="+"'"+account+"'"
    print(sql)
    r.execute(sql)
    db.commit()
    r.close()
    db.close()

if __name__ == '__main__':
    account = sys.argv[1]
    path = sys.argv[2]
    head(path=path,account=account)
