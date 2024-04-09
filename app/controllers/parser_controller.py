from flask import jsonify, request
from app.utils import read_file, save_file
from app.sunscript_parser import upload_files,compare_files


def compare():

    # Check if files are provided in the request
    if 'file1' not in request.files or 'file2' not in request.files:
        return jsonify({'error': 'Two files are required'}), 400
    
    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file2.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file1 and file1.filename.endswith('.world'):
        # Save the file to a desired location
        #file1.save('uploads/' + file1.filename)
        # mismatches =  compare_files('file1.txt', 'file2.txt')
        
        return jsonify({'message': 'calling Sunscript parser'}), 200
    else:
        return jsonify({'error': 'Invalid file type, must be a .world file'}), 400
    
    
    # Return the mismatches
    #return jsonify({'mismatches': mismatches})

def extract_save():
    # Check if files are provided in the request
    if 'file' not in request.files:
        return jsonify({'error': 'Two files are required'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
  
    
    if file and file.filename.endswith('.docx'):
        upload_files(file)
        return jsonify({'message': 'save in s3'}), 200
    else:
        return jsonify({'error': 'Invalid file type, must be a .world file'}), 400
    
    
    # Return the mismatches
    #return jsonify({'mismatches': mismatches})