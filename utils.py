import numpy as np
import pandas as pd
import settings
from transformers import BartTokenizer, BartForConditionalGeneration

summarizer = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

def get_summary(text, max_length=150):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = summarizer.generate(inputs, max_length=max_length, min_length=50, length_penalty=5., num_beams=2)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Format documented here https://docs.pinecone.io/docs/overview#upsert-and-query-vector-embeddings-with-the-pinecone-api
def transform_to_pinecone_format(dataset):
    for idx, entry in enumerate(dataset):
        # to avoid error "Metadata size is 53581 bytes, which exceeds the limit of 40960 bytes per vector"
        truncated_text = entry['metadata']['text'][:settings.MAX_TEXT_LENGTH]
        transformed = {
            'id': str(idx + 1), 
            'values': entry['values'],
            'metadata': {
                'pdf_file': entry['metadata']['pdf_file'],
                'text': truncated_text
            }
        }
        yield transformed

def iter_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

