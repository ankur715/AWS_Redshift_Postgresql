# library to connect to our Redshift (or PostgreSQL)
import psycopg2 as pg
import csv
tables = ["category", "customer", "product", "region",
          "salestransaction", "soldvia", "store", "vendor"]
def main():
    for i in range(len(tables)):
        # postgres database
        conn_str = "dbname='ZAGDB' host='localhost' port='5432' user='postgres' password='ankur715'"
        # connect to database
        print("\nConnecting to database {}:".format(tables[i]))
        conn = pg.connect(conn_str)
        # return a cursor object to perform PostgreSQL commands
        cursor = conn.cursor()
        # execute a database operation or query
        cursor.execute("SELECT * FROM {}".format(tables[i]))
        # retrieve the records from the database
        records = cursor.fetchall()
        # write records in csv files
        with open("{}.csv".format(tables[i]), 'w') as f:
            writer = csv.writer(f, delimiter=',')
            for record in records:
                writer.writerow(record)
        print(records)
        # finally, close the communication with the PostgreSQL
        cursor.close()
        conn.close()
# can also use try,except,finally block to catch error during process
# fetchone() fetches the next row in the result set as a single tuple
# fetchmany(size=cursor.arraysize) fetches the next set of rows specified
if __name__ == "__main__":
	main()
    # only if this file was run directly, and not imported
