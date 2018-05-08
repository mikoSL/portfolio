import boto3
import zipfile
import io
from io import StringIO
import mimetypes


s3 = boto3.resource('s3')

portfolio_bucket = s3.Bucket('portfolio.linafinland.com')
build_bucket = s3.Bucket('portfoliobuild.linafinland.com')

# io.BytesIO save zip file in memory instead of filesystem
portfolio_zip = io.BytesIO()
build_bucket.download_fileobj('portfoliobuild.zip',portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        #upload all build bucket file to portfolio bucket
        portfolio_bucket.upload_fileobj(obj,nm, 
    	  ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        #change permission to 'public read'
        portfolio_bucket.Object(nm).put(ACL='public-read')