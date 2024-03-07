import pandas as pd
from sentence_transformers import SentenceTransformer, util
from nltk.corpus import stopwords
stop = stopwords.words('english')


def text_preprocessing(text):
    # make all words with lower letters
    text = text.lower()
    # getting rid of any punctution
    # text = text.replace('http\S+|www.\S+|@|%|:|,|', '', case=False)
    # spliting each sentence to words to apply previous funtions on them
    word_tokens = text.split(' ')
    keywords = [item for item in word_tokens if item not in stop]
    # assemble words of each sentence again and assign them in new column

    return ' '.join(keywords)


df = pd.read_csv("data/dataset.csv").reset_index(drop=True)
embedding_df = pd.read_csv("data/embedding.csv", header=None)
docs = embedding_df.values
text = input("Your search: ")
# text = "a white shirt for men"

model = SentenceTransformer("bert-base-nli-mean-tokens")
query_vector = model.encode(text_preprocessing(text)).astype(float)

results = util.pytorch_cos_sim(query_vector, docs)

top_n = 5
sort_idx = results.argsort(descending=True, axis=1)[0][:top_n]
print(df.iloc[sort_idx])
