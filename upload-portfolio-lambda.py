import boto3
import zipfile
import io
from io import StringIO
import mimetypes

def lambda_handler(event, context):
    
    #config  sns
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:184139005054:deployPortfolioTopic')
    
    location = {
        'bucketName': 'portfoliobuild.linafinland.com'
        'objectKey': 'portfoliobuild.zip'
    }
    try:
        #codepipeline config
        job = event.get('CodePipeline.job')
        
        if job:
            for artifact in job['data']['inputArtifacts']:
                if artifact['name'] = 'MyAppBuild':
                    location = artifact['location']['s3Location']
        print ('Build portfolio from' + str(location))
        
        #sync portfolio and portfolio build buckets
        s3 = boto3.resource('s3')
        
        portfolio_bucket = s3.Bucket('portfolio.linafinland.com')
        build_bucket = s3.Bucket(location['bucketName'])
        
        # io.BytesIO save zip file in memory instead of filesystem
        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj(location['objectKey'],portfolio_zip)
        
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                #upload all build bucket file to portfolio bucket
                portfolio_bucket.upload_fileobj(obj,nm, 
                  ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                #change permission to 'public read'
                portfolio_bucket.Object(nm).put(ACL='public-read')
                
        #sns content
        topic.publish(Subject='Portofolio deployed', Message='Deploy portfolio successfully!')
        
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job['id'])
    except:
        topic.publish(Subject='Portofolio deploy failed', Message='Portfolio deployment failed')
        raise
    
    return 'hello deploy portfolio lambda function'