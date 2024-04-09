from app.utils import read_file,extract_paragraphs


def compare_files(file1, file2):
    # Read data from files
    data1 = read_file(file1)
    data2 = read_file(file2)

    # Make paragraphs
    paragraphs = extract_paragraphs(data1)

    # Connect paragraphs to AWS NER
    
    # Compare the data
    mismatches = []
    for item1, item2 in zip(data1, data2):
        if item1 != item2:
            mismatches.append((item1, item2))
    
    return mismatches