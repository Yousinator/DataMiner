import pandas as pd
import numpy as np
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances


class TextMiner:
    def __init__(self, docs, df):
        self.docs = docs
        self.docs = self.tokenize_docs(docs)
        self.docs = self.lowercase(docs)
        self.docs = self.remove_stopwords(docs)
        self.docs = self.remove_punctuation(docs)
        self.docs = self.stemmer(docs)
        self.df = df


    def tokenize_docs(self, docs):

        for x, doc in enumerate(docs):
            token = word_tokenize(doc)
            docs[x] = token
        return docs

    def lowercase(self, docs):
        for x, doc in enumerate(docs):
            docs[x] = [word.lower() for word in doc]
        return docs

    def remove_stopwords(self, docs):
        stop_words = set(stopwords.words('english'))
        for x, doc in enumerate(docs):
            docs[x] = [word for word in doc if word not in stop_words]
        return docs

    def remove_punctuation(self, docs):
        for x, doc in enumerate(docs):
            docs[x] = [word for word in doc if word.isalpha()]
        return docs

    def stemmer(self, docs):
        stemmer = PorterStemmer()
        for x, doc in enumerate(docs):
            docs[x] = [stemmer.stem(word) for word in doc]
        return docs

    def tf_idf(self, docs):
        for x, doc in enumerate(docs):
            docs[x] = " ".join(doc)

        tfidf = TfidfVectorizer()
        processed_docs = tfidf.fit_transform(docs)
        tfidf = pd.DataFrame(processed_docs.toarray(), columns=tfidf.get_feature_names_out(), index = [x for x in range(len(docs))])
        return tfidf

    def process_query(self, query):
        self.query = self.tokenize_docs(query)
        self.query = self.lowercase(query)
        self.query = self.remove_stopwords(query)
        self.query = self.remove_punctuation(query)
        self.query = self.stemmer(query)
        return query[0]

    def rank(self, df):
        cosine_similarity_result = []

        B = np.array(df.iloc[-1])
        B = B.reshape(1,-1)
        for x in range(df.shape[0] - 1):
            A = np.array(df.iloc[x])
            A = A.reshape(1,-1)

            cosine_similarity_result.append(cosine_similarity(A, B))
        sim_df = self.df.copy()
        sim_df["Similarity"] = [float(x.item()) for x in cosine_similarity_result]
        if (min(sim_df["Similarity"]) == 0 and max(sim_df["Similarity"])==0):
            return "There are no matching results"
        sim_df = sim_df[sim_df["Similarity"] != 0]
        percentile = np.percentile(sim_df["Similarity"], 90)
        final = sim_df[sim_df["Similarity"] >= percentile]
        final = sim_df[sim_df["Similarity"] >= (max(sim_df["Similarity"]) / 1.5)]


        return final.sort_values(by="Similarity", ascending=False, kind='heapsort')

    def structure_output(self, final):
        output = []
        for i, row in final.iterrows():
            name = self.df.iloc[i]["Name"]
            bio = self.df.iloc[i]["Bio"]
            similarity = row["Similarity"]
            output.append(f"[{round(similarity,3)}] {i}- {name}: {bio}")
        return output

    def print_output(self, output):
        for i, result in enumerate(output):
            print(result)

    def search(self,query):
        query = self.process_query([query])
        final_docs = self.docs.copy()
        final_docs.append(query)
        final_docs = self.tf_idf(final_docs)
        ranks = self.rank(final_docs)
        if type(ranks) != str:
            output = self.structure_output(ranks)
        else:
            output = "There are no matching results"
        return output, ranks

