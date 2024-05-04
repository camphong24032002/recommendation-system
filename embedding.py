import pandas as pd
from utils import text_preprocessing
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("bert-base-nli-mean-tokens")

df = pd.read_csv('./data/dataset.csv')
feature_cols = ["Brand", "Description", "Category_by_gender", "Color"]
values = df[feature_cols].values
overall_infos = []
for value in values:
    result = " ".join(value)
    overall_infos.append(result)
df["overall_info"] = overall_infos
df['cleaned_info'] = text_preprocessing(df['overall_info'])

df["embeddings"] = df["cleaned_info"].apply(lambda x: model.encode(x))
embedding_df = pd.DataFrame(df["embeddings"].tolist())
embedding_df.to_csv("./data/embedding.csv", header=None, index=0)
