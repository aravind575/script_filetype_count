from google.cloud import storage
from collections import defaultdict

# Replace with your Google Cloud project and bucket name
PROJECT_ID = "your-google-cloud-project-id"
BUCKET_NAME = "your-bucket-name"

def count_filetypes():
    # Initialize Google Cloud Storage client
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.get_bucket(BUCKET_NAME)
    
    # Initialize a dictionary to store filetype counts
    filetype_counts = defaultdict(int)
    
    # List all blobs in the bucket
    blobs = bucket.list_blobs()
    
    for blob in blobs:
        if blob.metadata and "filetype" in blob.metadata:
            filetype = blob.metadata["filetype"]
            filetype_counts[filetype] += 1

    return filetype_counts

if __name__ == "__main__":
    counts = count_filetypes()
    for filetype, count in counts.items():
        print(f"{filetype}: {count}")
