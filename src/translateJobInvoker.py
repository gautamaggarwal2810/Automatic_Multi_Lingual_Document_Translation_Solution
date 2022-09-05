

import json
from urllib.parse import unquote_plus
import os
from awsUtils import AwsUtils

from datetime import datetime
# Get the service resources
aws_utils = AwsUtils(os.environ['AWS_REGION'])


def lambda_handler(event, context):

    aws_utils = AwsUtils()
    data_access_role_arn = os.environ['BATCH_TRANSLATION_ROLE']
    batchInputS3URI =  os.environ['BATCH_INPUT_S3URI']
    batchOutputS3URI =  os.environ['BATCH_OUTPUT_S3URI']
    parallelDataName =  os.environ['PARALLEL_DATA_NAME']
    print(data_access_role_arn)

    now = datetime.now() # current date and time
    date_time = now.strftime("-%m%d%Y%H%M%S")
    jobName = "translateBatchJob" + date_time
    parallelDataNames = None

    if aws_utils.checkParallelDataJob( parallelDataName ):
        parallelDataNames = [parallelDataName]
    # initiate asyncrhonous batch translation job with translate client
    response = aws_utils.start_translate_batch_job( jobName, batchInputS3URI,
    batchOutputS3URI, data_access_role_arn, parallelDataNames )

    return {
        'statusCode': 200,
        'body': json.dumps('Initiated Translate Batch Job')
    }
