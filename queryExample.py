from sentence_transformers import SentenceTransformer
import torch
import pinecone
import settings
import utils

PINECONE_API_KEY = settings.PINECONE_API_KEY
PINECONE_ENV = settings.PINECONE_ENV

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
model

# Enter desired query here
query = "Foreign trade sanctions"

# create the query vector
xq = model.encode(query).tolist()

index_name = "semantic-pdf"
index = pinecone.GRPCIndex(index_name)

xc = index.query(xq, top_k=5, include_metadata=True)

for result in xc['matches']:
    summary = utils.get_summary(result['metadata']['text'])
    print(f"{round(result['score'], 2)} Match - id: {result['id']}, pdf_file: {result['metadata']['pdf_file']}, text summary: {summary}")