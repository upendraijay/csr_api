from app.utils import read_file,extract_paragraphs,upload_to_s3

def upload_files(file):
    print("inside upload file")
    # Read data from files
    data = read_file(file)
    
    # Make paragraphs
    paragraphs = extract_paragraphs(data)

    # Upload paragraphs to S3
    upload_to_s3(paragraphs)
    
    return "Done"