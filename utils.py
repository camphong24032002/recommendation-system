from sentence_transformers import util
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


def concat_content(title, value):
    return f"{title}: {value}"


def df_to_text(df):
    text = []
    titles = ["Product ID", "Product Name", "Gender", "Price (INR)", "Primary Color"]
    cols = ["ProductID", "ProductName", "Gender", "Price (INR)", "PrimaryColor"]
    for idx in range(df.shape[0]):
        for title, col in zip(titles, cols):
            text.append(concat_content(title, df[col].iloc[idx]))
        text.append('-------------------------------')
    return '<br>'.join(text)


def get_chat_response(model, df, docs, text):
    query_vector = model.encode(text_preprocessing(text)).astype(float)
    results = util.pytorch_cos_sim(query_vector, docs)
    top_n = 3
    sort_idx = results.argsort(descending=True, axis=1)[0][:top_n]
    return df.iloc[sort_idx]
