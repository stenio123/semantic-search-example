from datasets import load_dataset
from datasets import Dataset

hf_dataset = Dataset.from_file(filename="/Users/stenio123/Downloads/master-gdc-gdcdatasets-2020445568-2020445568/dataset/data/data-00000-of-00001.arrow")

hf_dataset.push_to_hub("stenio123/1000GovPdfLibraryCongress-vector")