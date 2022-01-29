
import boto3
import logging

logger = logging.getLogger("listfile")

# Modify it before deployment
BUCKET = "test_bucket"


def list_files(prefix: str = ''):
    """list files given s3 prefix
    reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
    By default the action returns up to 1,000 key names. 
    Args:
        bucket (str): bucket name
        prefix (str, optional): [description]. Defaults to ''.
    Returns:
        [type]: [description]
    """
    contents = []
    success = True
    s3_bucket = boto3.resource('s3').Bucket(BUCKET)

    try:
        for _file in s3_bucket.objects.filter(Prefix=prefix):
            if _file.key.endswith("/"):
                continue
            contents.append(_file.key)
    except:
        logger.error("List file failed\n\n", exc_info=True)
        success = False
    return contents, success
