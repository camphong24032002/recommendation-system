# Fashion Product Recommendation System

## Dataset

This system uses the dataset from [kaggle](https://www.kaggle.com/datasets/shivamb/fashion-clothing-products-catalog).

**About this Dataset**: Fashion Clothing Product Catalog from Myntra.com.

Myntra is a major Indian fashion e-commerce company headquartered in Bengaluru, Karnataka, India. The company was founded in 2007 to sell personalized gift items. In May 2014, Myntra.com was acquired by Flipkart.

**Attributes**: ProductID, ProductName, ProductBrand, Gender, Price (INR), NumImages, Description, PrimaryColor.

## Embedding Model

The model I have used is [bert-base-nli-mean-tokens](https://huggingface.co/sentence-transformers/bert-base-nli-mean-tokens)

This is a sentence-transformers model: It maps sentences & paragraphs to a 768 dimensional dense vector space and can be used for tasks like clustering or semantic search.

In this system, I select these attributes for embeddings:
`ProductName`, `ProductBrand`, `Gender`, `Description`, `PrimaryColor`.

## How it works

First, we need to preprocess the data and combine the potential attributes into a singular sentence.

Next, we'll employ an embedding model to transform the crafted sentence into its vector representation

For convenience, I have embedded the data and stored it to embedding.csv

Finally, to engage with our recommendation engine, simply encode the input query into an embedding and fetch the recommendations utilizing cosine similarity to measure the matches.

## How-to use

- First, you need to clone this repository.
- Install the libraries:
```bash
pip install -r requirements.txt
```
- To run the system, type
```bash
python main.py
```
- Finally, please enter your query, and the recommendation system will generate a list of the top five products that most closely match your specifications.