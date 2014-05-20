import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='saffron_db')



def saffron_db(query):
    cur = conn.cursor()
    cur.execute(query)
    #cur.execute("INSERT INTO News (Link_news, Text_news, Category_news, Title_news, TIME, Num_view_news) VALUES (?)")
    conn.commit()
    cur.close()



#cur.execute("SELECT * FROM users")
#conn.close()


#print(cur.description)

#
#for row in cur:
#    id = row[0]
#    username = row[1]
#    password = row[2]
#    print(password)

