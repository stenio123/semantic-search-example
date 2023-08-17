import pinecone
from datasets import load_dataset
import settings
import utils
import time
import numpy as np

PINECONE_API_KEY = settings.PINECONE_API_KEY
PINECONE_ENV = settings.PINECONE_ENV

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)


hf_dataset = load_dataset("stenio123/1000GovPdfLibraryCongress-vector", split="train")
print(hf_dataset.column_names) #values, metadata{pdf_file, text}
print(len(hf_dataset))

pinecone_data = list(utils.transform_to_pinecone_format(hf_dataset))

index_name = "semantic-pdf"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        name=index_name,
        dimension=len(pinecone_data[0]['values']),
        metric='cosine'
    )
    # wait a moment for the index to be fully initialized
    time.sleep(1)

# now connect to the index
index = pinecone.GRPCIndex(index_name)

for batch in utils.iter_batches(pinecone_data, batch_size=25):
    index.upsert(vectors=batch)