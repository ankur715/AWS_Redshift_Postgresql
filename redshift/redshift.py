import psycopg2

ztables = ["category", "region", "vendor", "product",
         "store", "customer", "salestransaction", "soldvia"]
# sql tables created and saved, load into redshift using copy
def redshift():
    conn_string = psycopg2.connect(dbname='dev', host='redshift-cluster-1.cogamnpawfrb.us-east-2.redshift.amazonaws.com',
                                   port='5439', user='ankur', password='Ankur715')
    cur = conn_string.cursor();
    file = open("ZAGI-tables.sql", 'r')
    cur.execute(file.read())
    conn_string.commit()
    for i in ztables:
        # copy data from s3 files to redshift
        sql = """copy {} from 's3://ankur-zagiiii-bucket/{}.csv' credentials 'aws_iam_role=arn:aws:iam::927492682481:role/myRedshiftRole' delimiter ',' region 'us-west-2';""".format(i,i)
        cur.execute(sql)
        conn_string.commit()
        print("Copied {}".format(i))
redshift()

#
#

#
# conn_string = psycopg2.connect(dbname='dev', host='redshift-cluster-1.cogamnpawfrb.us-east-2.redshift.amazonaws.com',
#                                port='5439', user='ankur', password='Ankur715')
# cur = conn_string.cursor();
#
# file = open("ZAGI-tables.sql", 'r')
# cur.execute(file.read())
# conn_string.commit()
#
# for i in ztables:
#     sql = """copy {} from 's3://ankur-zagiiii-bucket/{}.csv'
#         credentials 'aws_iam_role=arn:aws:iam::927492682481:role/myRedshiftRole'
#         delimiter ',' region 'us-west-2';""".format(i,i)
#     cur.execute(sql)
#     conn_string.commit()
#
#


# conn_string = psycopg2.connect(dbname='dev', host='redshift-cluster-1.cogamnpawfrb.us-east-2.redshift.amazonaws.com', port='5439', user='ankur', password='Ankur715')
# cur = conn_string.cursor();
#
# file = open("salestransaction.sql", 'r')
# cur.execute(file.read())
# conn_string.commit()
#
# sql = """copy salestransaction from 's3://ankur-zagiiii-bucket/salestransaction.csv' credentials 'aws_iam_role=arn:aws:iam::927492682481:role/myRedshiftRole' delimiter ',' region 'us-west-2';"""
# cur.execute(sql)
# conn_string.commit()