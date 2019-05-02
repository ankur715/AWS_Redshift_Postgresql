# AWS SDK for python, amazon s3
import boto3

### list of amazon s3 buckets
# s3 client
s3 = boto3.client('s3')
# s3 to list current buckets
response = s3.list_buckets()
print(response)
# empty, no buckets created
# list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Prior Bucket List: %s" % buckets)

### create amazon s3 bucket and upload files
s3.create_bucket(Bucket="ankur-zagiiiiii-bucket",
                 CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
files = ["category.csv", "customer.csv", "product.csv",
         "region.csv", "salestransaction.csv", "soldvia.csv",
         "store.csv", "vendor.csv"]
for i in files:
    # upload files to the bucket
    s3.upload_file(i, "ankur-zagiiiiii-bucket", i)