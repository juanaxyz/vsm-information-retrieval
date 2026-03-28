import math


def hitung_norm(weight_vector):          # √(Σw²)
    return math.sqrt(sum(w ** 2 for w in weight_vector))

def hitung_cosine(vec_q, vec_d):        # Sum(Q*D) / (|Q|×|D|)
    return sum(q * d for q, d in zip(vec_q, vec_d)) / (hitung_norm(vec_q) * hitung_norm(vec_d))

def ranking(query, docs, tfidf_matrix):  # return DataFrame terurut
    for i, doc in enumerate(docs):
        print("=="*20)
        print(f"Document {i+1}: {doc}")
        print(f"TF-IDF Vector: {tfidf_matrix[i]}")

        # hitung 
        cos_sim = hitung_cosine()
    # return tfidf_matrix

query = ['ajar', 'machine', 'learning']
term = ['ajar', 'anjlok', 'banyak', 'ihsg', 'jual', 'learning', 'machine', 'sangat', 'senang', 'suka', 'tarik']
docs = [['suka', 'ajar', 'machine', 'learning'], ['machine', 'learning', 'sangat', 'tarik'], ['ajar', 'machine', 'learning', 'senang'], ['suka', 'ajar', 'machine', 'learning'], ['ihsg', 'anjlok', 'banyak', 'jual']]

matrix = [[0.9808292530117263, 0.0, 0.0, 0.0, 0.0, 0.8109302162163288, 0.8109302162163288, 0.0, 0.0, 1.252762968495368, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.8109302162163288, 0.8109302162163288, 1.791759469228055, 0.0, 0.0, 1.791759469228055], [0.9808292530117263, 0.0, 0.0, 0.0, 0.0, 0.8109302162163288, 0.8109302162163288, 0.0, 1.791759469228055, 0.0, 0.0], [0.9808292530117263, 0.0, 0.0, 0.0, 0.0, 0.8109302162163288, 0.8109302162163288, 0.0, 0.0, 1.252762968495368, 0.0], [0.0, 1.791759469228055, 1.791759469228055, 1.791759469228055, 1.791759469228055, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

ranking(query,docs, matrix)
