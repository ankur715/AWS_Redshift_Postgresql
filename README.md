## <div align="center">AWS Redshift Cluster 
### ZAGI retail company sales department database
<p align="left">
  <img width="600" height="250" src="https://github.com/ankur715/AWS_redshift/blob/master/postgresql-to-redshift.jpg"> 
</p>

---

#### **STEPS**
#### *Note: Includes links to downloads/instructions; varies according to OS (mine is Windows); single ETL cluster*
1. **ZAGDB (.sql in this repo for reference)**

2. **PostgreSQL (https://www.postgresql.org/download/)**

3. **pfAdmin (https://www.pgadmin.org/download/pgadmin-4-windows/)**

4. **Create ZAGDB database on pdAdmin**
    - *Note down credentials*
    - CREATE TABLE
    - INSERT VALUES
<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/postgres/ZAGDB%20PostgreSQL.png"> 
</p>

5. **PyCharm (https://www.jetbrains.com/pycharm/download/)**
    - Back-End coding! 
<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/pgsql/pgsql1 .png"> 
</p>

*Data extracted and saved*

<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/pgsql/pgsql2 .png"> 
</p>

6. **Amazon AWS (https://aws.amazon.com/)**

7. **AWS S3 (https://s3.console.aws.amazon.com/s3/home?region=us-east-2)**
<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/s3/s3%20pycharm.png"> 
</p>

*Data loaded on AWS S3 Bucket*

<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/s3/s3%20bucket.png"> 
</p>

8. **AWS Redshift Cluster steps 1-5 (https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)**
<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/AWS/redshift-cluster-1.png"> 
</p>

*Note down the username and password*

9. **AWS Redshift (https://us-east-2.console.aws.amazon.com/redshift/home?region=us-east-2#)**
<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/redshift/redshift%20pycharm.png"> 
</p>

Ways to query:
  - Redshift Query Editor:
<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/redshift/redshift%20aws.png"> 
</p>

  - PyCharm Execute Query
<p align="left">
  <img width="1000" height="500" src="https://github.com/ankur715/AWS_redshift/blob/master/redshift/redshift%20pycharm%20query.png"> 
</p>


### Virtual Environment:
  - Extra option if switching between different versions.   
  - Python virtual environments allow developers to control software dependencies in Python code. They're useful ways of ensuring that the correct package/library versions are consistently used every time the software runs. Virtual environments also help ensure that the results from running code are reproducible. 
<p align="left">
  <img width="600" height="250" src="https://github.com/ankur715/AWS_Redshift_Postgresql/blob/master/venv/pics/activate_venv.png"> 
</p>

---

If you would like to discuss my project or any new opportunities, please email me at [p.ankur.715@gmail.com](mailto:p.ankur.715@gmail.com) or https://www.linkedin.com/in/ankurpatel715/.
