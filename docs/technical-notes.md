# Technical Notes

## Model Selection
- Uses pretrained sentiment analysis model [DistilBERT from Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/distilbert).
- Chosen for:
    - DistilBERT reaches about *90 to 92 percent* accuracy on the SST-2 benchmark, which is considered strong baseline performance for sentiment analysis.
    - No fine-tuning or optimization is required for the MVP because DistilBERT provides strong baseline accuracy and fast CPU inference out of the box.
    - DistilBERT is well-suited for MVP use because it balances accuracy and speed without requiring GPU hardware or model fine-tuning.
    - DistilBERT also has a small memory footprint compared to full BERT, which keeps local processing light.

## Data Pipeline Overview
### Loading Data
- Dataset sourced from [HuggingFace (Amazon Reviews 2023)](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023)
    - Note: The Amazon 2023 dataset is extremely large, so for the MVP PulseEQ works with the **Toys & Games** subset and additional filters to keep processing manageable.
  - Implementation detail: PulseEQ pins the `datasets` library to a 2.x version because this dataset currently relies on a script-based loader that is not supported in newer 3.x releases.
- This dataset is included for example purposes only. Companies that are interested in sentiment analysis should use their own current datasets or plan to collect data that aligns with the specific insights they want to generate.
- A good dataset for sentiment analysis should include clear text reviews, relevant metadata such as product or category information, and enough examples to reflect a range of customer opinions. Higher quality datasets also avoid duplicated entries, contain minimal noise, and represent the audience or domain a company wants to understand.

### Filtering
- PulseEQ first filters the dataset to the **Toys & Games** category, then further narrows it using simple keyword matching (for example, “Mattel,” “Barbie,” “Hot Wheels”) to approximate toys sold by Mattel. This creates a focused subset of reviews with enough sentiment variation to demonstrate the workflow while keeping processing lightweight.
    - In production scenarios, companies should apply filters aligned with their goals, such as brand, category, SKU, or product line. Filtering ensures that only relevant items are passed to the sentiment model.

### AI Enrichment

#### Sentiment Classification
- Uses [HuggingFace transformers library](https://huggingface.co/docs/transformers/en/index)
    - For each review:
        - Extract the sentiment label (positive, negative, or neutral) and the associated confidence score from the model's output.
        - Store the label and score alongside the product title and review body.

#### Topic/category tagging
- TK

#### AI-generated Product Labels
- Because the dataset lacks product names, PulseEQ uses AI to generate a short product label from the ASIN and review text. This enables clean product grouping and visualization without relying on external catalogs. The generated `product_label` is used throughout the analytics pipeline.

### Visualization Approach
- Uses matplotlib for MVP.
    - Matplotlib is used for the MVP because it is lightweight, widely supported, and requires no additional UI dependencies.
- Displays sentiment distribution (bar or pie chart).

## Export Strategy
- CSV export via pandas
    - product_title
    - review_body
    - sentiment_label
    - sentiment_score

## Performance Considerations
- DistilBERT provides strong baseline accuracy with fast CPU inference. For this MVP, inference speed is more than sufficient because the analysis is run on a filtered subset of reviews rather than at full production scale. 
    - Larger datasets or real-time systems may require performance optimizations such as batching, GPU acceleration, or model distillation, but these are out of scope for the MVP.
    - *MVP GOAL* : Process a medium-sized dataset (around 5,000–10,000 reviews) in under one minute on a typical laptop CPU.
        - In production environments, companies often speed up processing by using cloud compute resources such as larger CPU clusters or GPU nodes. These enhancements are not needed for the MVP but are commonly used for high-volume workloads.
- Future:
    - Batch inference - means processing reviews in groups so the model can work faster.
        - PulseEQ runs the sentiment model locally, so there are no external API rate limits to consider. In a hosted or API-based deployment, companies would need to account for request caps and quotas by batching reviews, throttling requests, or using higher-throughput plans.
    - GPU support (future enhancement with associated infrastructure costs)
    - Async pipeline - async processing lets the system work on several batches of reviews at the same time, which speeds up analysis for very large datasets. This usually requires extra computing resources running in parallel, so it comes with added infrastructure costs.
        - Larger, production-grade deployments might use a message queue to coordinate asynchronous processing across multiple workers. This allows many batches of reviews to be processed in parallel, but it also introduces additional infrastructure components and operational cost.

## Environment Notes
- PulseEQ is developed in Python 3.9.6 for local compatibility, but the codebase can be upgraded to Python 3.10 or 3.11 in the future if needed for performance or library support.
- A local virtual environment is used to isolate project dependencies.
    - The virtual environment directory (pulse-venv/) is not included in version control and is ignored via .gitignore.
- The project structure follows a simple readable layout:

```
pulse_eq/
├── docs/               # Project documentation
├── src/                # Python source code
├── data/               # Optional example datasets
├── requirements.txt    # Dependency list
├── .gitignore
└── README.md
```
- All installed libraries are captured in [`requirements.txt`](../requirements.txt)

### Image Handling (Future Enhancement)
While the MVP does not use image data, PulseEQ retains awareness of the `images` field for future enhancements. Many negative reviews include photos showing defects (e.g., damage, missing parts). A later version may analyze these images to validate negative review claims or identify recurring quality issues. This would enable a deeper understanding of root causes behind negative sentiment, but is out of scope for the MVP.








