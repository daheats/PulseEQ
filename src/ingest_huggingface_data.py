#Path handling for saving/loading local files
from pathlib import Path

#HuggingFace Datasets library for loading and processing dataset objects
from datasets import load_dataset

#For DataFrame-based data cleaning, exploration, and manipulation
import pandas as pd

# Load a reviews dataset from HuggingFace and return it
def load_customer_reviews():
    dataset = load_dataset(
        "McAuley-Lab/Amazon-Reviews-2023",
        "raw_review_Toys_and_Games",
        trust_remote_code=True

    )
    return dataset


if __name__ == "__main__":
    customer_reviews_dataset = load_customer_reviews()
    print(customer_reviews_dataset)
    print(customer_reviews_dataset[0])
