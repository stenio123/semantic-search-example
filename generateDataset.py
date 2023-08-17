import os
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from datasets import Dataset
import settings

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = " ".join(page.extract_text() for page in reader.pages)
    return text

model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')  # Change to 'cuda' if you have a GPU

pdf_folder = settings.PDF_FOLDER
dataset_file_output_folder = settings.DATASET_FILE_OUPUT_FOLDER
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith('.pdf')]

dataset = {
    'documents': []
}

error_files = []
successful_files = 0

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    try:
        text = extract_text_from_pdf(pdf_path)
        vector = model.encode(text).tolist()
        dataset['documents'].append({
            'values': vector,
            'metadata': {
                'text': text,
                'pdf_file': pdf_file
            }
        })
        print(f"Done with {pdf_file}")
        successful_files += 1
    except Exception as e:
        print(f"Error processing {pdf_file}: {e}")
        error_files.append(pdf_file)

hf_dataset = Dataset.from_dict({'values': [item['values'] for item in dataset['documents']],
                                'metadata': [item['metadata'] for item in dataset['documents']]})

hf_dataset.save_to_disk(dataset_file_output_folder)


print(f"Total PDFs processed: {len(pdf_files)}")
print(f"Number of successful PDFs: {successful_files}")
print(f"Number of PDFs with errors: {len(error_files)}")
if error_files:
    print("Files with errors:")
    for err_file in error_files:
        print(err_file)

# To upload to Huggingface:
#huggingface-cli login
#huggingface-cli dataset upload /path/to/save/dataset --name your_dataset_name
