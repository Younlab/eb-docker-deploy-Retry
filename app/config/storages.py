from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    'S3StaticStorage',
    'S3DefaultStorage',
)

# static file
class S3StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = 'static'

# media file
class S3DefaultStorage(S3Boto3Storage):
    default_acl = 'private'
    location = 'media'