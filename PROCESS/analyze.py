import psycopg2

conn_string = psycopg2.connect(dbname='dev', host='redshift-cluster-1.cogamnpawfrb.us-east-2.redshift.amazonaws.com',
                               port='5439', user='ankur', password='Ankur715')
cur = conn_string.cursor();

cur.execute("SELECT p.productname, v.vendorname FROM product p, vendor v WHERE p.vendorid=v.vendorid AND productprice<(SELECT AVG(productprice) FROM product);")
results = cur.fetchall()
print(results)
