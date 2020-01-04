from scrapy.cmdline import execute

execute("scrapy crawl jianshu_spider".split(" "))

'''
import pymysql

db = pymysql.connect(host="127.0.0.1", user='root', password="smh8532557", database='zoo')
print(db)
cursor = db.cursor()


try:
    sql = "insert into article(title, name, url, collection) values (%s, %s, %s, %s)"
    # 通过游标完成CRUD
    cursor.execute(sql, ['我是标题', '作者名称', 'url地址', '文艺，科技，娱乐'])
    # 默认需要手动提交事物
    db.commit()
except:
    print("sql插入出错")
    db.rollback()


try:
    sql = "update article set title=%s, name=%s where id=%s"
    # 返回的是受影响的行数
    count = cursor.execute(sql, ['新标题', '老作者', 2])
    # 默认需要手动提交事物
    db.commit()
except:
    print("sql更新出错")
    db.rollback()



try:
    sql = "select * from article where id = %s"
    # 返回的是受影响的行数
    cursor.execute(sql, [2])
    # 查询不需要提交事物，但是要通过fatch完成数据的抓取
    print(cursor.fetchone())
except:
    print("sql查询出错")
    db.rollback()


try:
    keyword = '标题'         # 查询结果以title字段为主包含'标题'的字符串
    current_page = 2        # 第二页
    size = 3                # 一次查询三条数据
    sql = "select * from article where title like %s limit %s, %s"
    # 返回的是受影响的行数,没有0页，current_page最小值是1，所以只能current_page - 1
    cursor.execute(sql, [f'%{keyword}%', (current_page - 1), size])
    # 查询不需要提交事物，但是要通过fatch完成数据的抓取
    for row in cursor.fetchall():
        print(row)

except:
    print("sql查询出错")
    db.rollback()

finally:
    cursor.close()
'''
