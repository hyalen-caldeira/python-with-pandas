import boto3

class S3FileManager:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.s3 = boto3.client('s3',
                               aws_access_key_id=aws_access_key_id,
                               aws_secret_access_key=aws_secret_access_key,
                               region_name=region_name)

    def upload_file_to_s3(self, file_path, bucket_name, object_name):
        try:
            self.s3.upload_file(file_path, bucket_name, object_name)
            print(f"File uploaded successfully to bucket: {bucket_name}, object: {object_name}")
        except Exception as e:
            print(f"Error uploading file to S3: {e}")

# Example usage
if __name__ == "__main__":
    # AWS credentials and region
    aws_access_key_id = 'hyalen_access_key_id'
    aws_secret_access_key = 'hyalen_secret_access_key'
    region_name = 'hyalen_region'

    # Initialize S3 file manager
    s3_file_manager = S3FileManager(aws_access_key_id, aws_secret_access_key, region_name)

    # Local file path
    file_path = 'local_file.txt'

    # S3 bucket and object names
    bucket_name = 'hyalen_bucket_name'
    object_name = 'destination_folder/file.txt'

    # Upload file to S3
    s3_file_manager.upload_file_to_s3(file_path, bucket_name, object_name)
