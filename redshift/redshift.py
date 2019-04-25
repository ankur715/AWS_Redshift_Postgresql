import psycopg2

ztables = ["product", "category"]
# sql tables created and saved, load into redshift using copy
def redshift():
    conn_string = psycopg2.connect(dbname='dev', host='redshift-cluster-1.cogamnpawfrb.us-east-2.redshift.amazonaws.com',
                                   port='5439', user='ankur', password='Ankur715')
    cur = conn_string.cursor();
    for i in range(len(ztables)):
        file = open("{}.sql".format(ztables[i]), 'r')
        cur.execute(file.read())
        conn_string.commit()
        # copy data from s3 files to redshift
        sql = """copy {} from 's3://ankur-zagiiii-bucket/{}.csv' credentials 'aws_iam_role=arn:aws:iam::927492682481:role/myRedshiftRole' delimiter ',' region 'us-west-2';""".format(ztables[i],ztables[i])
        cur.execute(sql)
        conn_string.commit()
        print("Copied {}".format(ztables[i]))
        # show entire table
        cur.execute("select * from {};".format(ztables[i]))
        results = cur.fetchall()
        print(results)
redshift()




# conn_string = psycopg2.connect(dbname='dev', host='redshift-cluster-1.cogamnpawfrb.us-east-2.redshift.amazonaws.com', port='5439', user='ankur', password='Ankur715')
# cur = conn_string.cursor();
#
# file = open("ZAGI-tables.sql", 'r')
# cur.execute(file.read())
# conn_string.commit()
#
# sql = """copy category from 's3://ankur-zagiiii-bucket/category.csv' credentials 'aws_iam_role=arn:aws:iam::927492682481:role/myRedshiftRole' delimiter ',' region 'us-west-2';"""
# cur.execute(sql)
# conn_string.commit()
#
# cur.execute("select * from category;")
# results = cur.fetchall()
# print(results)



# conn_string = psycopg2.connect(dbname='dev', host='redshift-cluster-1.cogamnpawfrb.us-east-2.redshift.amazonaws.com', port='5439', user='ankur', password='Ankur715')
# cur = conn_string.cursor();
#
# file = open("product.sql", 'r')
# cur.execute(file.read())
# conn_string.commit()
#
# sql = """copy product from 's3://ankur-zagiiii-bucket/product.csv' credentials 'aws_iam_role=arn:aws:iam::927492682481:role/myRedshiftRole' delimiter ',' region 'us-west-2';"""
# cur.execute(sql)
# conn_string.commit()
#
#
# cur.execute("select * from product;")
# results = cur.fetchall()
# print(results)
