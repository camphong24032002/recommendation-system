from utils import get_chat_response, df_to_text
import pandas as pd
from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer

# For the first time, you need to download the stopwords
# import nltk
# nltk.download('stopwords')

from nltk.corpus import stopwords
stop = stopwords.words('english')

df = pd.read_csv("data/dataset.csv").reset_index(drop=True)
embedding_df = pd.read_csv("data/embedding.csv", header=None)
docs = embedding_df.values
model = SentenceTransformer("bert-base-nli-mean-tokens")


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("msg")
    res_msg = ""
    try:
        output_df = get_chat_response(model, df, docs, msg)
        output_text = df_to_text(output_df)
        res_msg = jsonify({"response": True, "message": output_text})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        res_msg = jsonify({"message": error_message, "response": False})
    return res_msg


if __name__ == "__main__":
    app.run(debug=True)
