# This is the __init__.py file for the utils package

# Import modules to make them available when the package is imported
from .file_utils import read_file, save_file,extract_paragraphs
from .s3_utils import upload_to_s3

# Optionally, you can define variables or constants accessible when the package is imported
MY_CONSTANT = 42

# You can also define functions or classes here
def my_utility_function():
    pass

# With this setup, when you import the utils package elsewhere in your Flask application 
#(such as in app/__init__.py or app/routes.py), you can access the functions, classes, variables, 
#or constants defined within the __init__.py file