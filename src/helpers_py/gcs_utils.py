'''
This module provides functions for uploading and downloading files to/from GCS buckets.
'''

import os
from google.cloud import storage  # type: ignore[import-untyped]
from google.cloud.exceptions import GoogleCloudError  # type: ignore[import-untyped]
from dotenv import load_dotenv

# Load environment variables at the top of the file
load_dotenv()

# Global variables for lazy initialization
_bucket_name = None
_storage_client = None

def _get_bucket_name():
    """Get bucket name from environment variable."""
    global _bucket_name
    if _bucket_name is None:
        _bucket_name = os.getenv('BUCKET_NAME')
        if not _bucket_name:
            raise RuntimeError('BUCKET_NAME environment variable is required.')
    return _bucket_name

def _get_storage_client():
    global _storage_client
    if _storage_client is None:
        _storage_client = storage.Client()  # Automatically uses ADC or env var or metadata server
        print("Initialized GCS client using Application Default Credentials.")
    return _storage_client


def download_from_gcs(remote_path: str):
    '''Downloads a file from GCS to /tmp and returns the local path.'''
    try:     
        blobname = remote_path
        bucket_name = _get_bucket_name()
        client = _get_storage_client()

        local_path = f'/tmp/{os.path.basename(blobname)}'
        bucket = client.bucket(bucket_name)  # type: ignore[misc]
        blob = bucket.blob(blobname)  # type: ignore[misc]
        blob.download_to_filename(local_path)  # type: ignore[misc]

        print(f'Downloaded {blobname} from {bucket_name} to {local_path}')
        return local_path
    except GoogleCloudError as e:
        print(f'Failed to download {remote_path}: {e}')
        raise


def upload_to_gcs(local_path: str, dirname: str, filename: str):
    '''Uploads a file to GCS.'''
    try:
        blobname = os.path.join(dirname, filename)
        bucket_name = _get_bucket_name()
        client = _get_storage_client()
        
        bucket = client.bucket(bucket_name)  # type: ignore[misc]
        blob = bucket.blob(blobname)  # type: ignore[misc]
        blob.upload_from_filename(local_path)  # type: ignore[misc]

        print(f'File {local_path} uploaded to {bucket_name}/{blobname}.')
        return True
    except GoogleCloudError as e:
        print(f'Failed to upload {local_path} to GCS: {e}')
        return False

