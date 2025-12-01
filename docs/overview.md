# Product Overview
PulseEQ is a sentiment analysis tool that converts raw customer reviews into clear and actionable insights. It automatically loads and filters review data, runs a pre-trained machine learning model to classify sentiment, and presents the results through intuitive visualizations and exportable datasets. PulseEQ makes it easy for users to understand what customers are thinking at scale and in seconds.

For this example, PulseEQ focuses on reviews for Mattel products. Mattel generates a wide range of toy reviews, which creates a diverse mix of sentiment that is useful for demonstrating the analysis workflow. This choice is for demonstration only. Companies should rely on their own datasets or collect data that aligns with the insights they want to generate.

## Problem Statement
Product teams face a constant challenge when trying to extract meaningful patterns from large volumes of customer feedback. Manual review is slow, inconsistent, and hard to scale. PulseEQ streamlines this process by using AI to classify sentiment and surface clear and actionable insights. Teams can understand what customers are saying without investing in heavy analytics or specialized data science skills.

## Goals
1. Provide simple and reliable sentiment analysis.
2. Make insights accessible through visualizations and exports.
3. Keep the workflow lightweight and easy to use.

## Success Criteria
1. Users can load a dataset and receive labeled sentiment results within seconds.
2. Accuracy aligns with the baseline performance expected from a pre-trained DistilBERT sentiment model.
3. Users can view clear visual summaries of sentiment distribution.
4. Users can export the processed results for further analysis or reporting.

## MVP Core Feature Set
1. Load Dataset
    - Load the input dataset programmatically (e.g., HuggingFace, local file, or configurable source).
    - Handle missing fields or load errors gracefully.

2. Filter Out Non-Relevant Items
- For this example, filter the dataset to include products from Mattel. This creates a focused subset of toy reviews while still offering a wide range of sentiment for demonstration.
    - In practice, companies should filter their own datasets based on the brands, categories, or product lines they want to analyze.

3. Sentiment Analysis
    - Apply a pretrained model (DistilBERT) to generate:
        - sentiment_label (positive, negative, neutral)
        - sentiment_score
    *No custom model training required for MVP.*

4. Display Sentiment Results
    - Generate a visual representation of sentiment distribution (e.g., bar or pie chart).
    - Chart may render in notebook, console window, or simple UI.

5. Export Processed Data
    - Export a CSV containing:
        - product_title
        - review_body
        - sentiment_label
        - sentiment_score
    - Enable easy sharing and further analysis.



