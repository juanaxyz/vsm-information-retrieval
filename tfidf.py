from collections import Counter
import math

def hitung_tf(doc, term):
    freq = Counter(doc)
    return {t: freq.get(t, 0) for t in term}

def hitung_df_per_term(t, docs_list):
    return sum(1 for d in docs_list if t in d)

def hitung_idf(df, N):
    return math.log(N / df) + 1

def hitung_weight(tf, idf):
    return tf * idf

def build_tfidf_matrix(docs, query, term, N):
    # DF & IDF dihitung sekali di luar loop
    df_map  = {t: hitung_df_per_term(t, docs) for t in term}
    idf_map = {t: hitung_idf(df_map[t], N) for t in term}

    # TF & Weight untuk setiap dokumen
    tf_matrix     = []
    weight_matrix = []
    for doc in docs:
        tf = hitung_tf(doc, term)
        tf_matrix.append({t: tf.get(t, 0) for t in term})
        weight_matrix.append({t: hitung_weight(tf.get(t, 0), idf_map[t]) for t in term})

    # TF & Weight untuk query
    tf_query     = hitung_tf(query, term)
    weight_query = {t: hitung_weight(tf_query.get(t, 0), idf_map[t]) for t in term}

    return {
        "df_map"       : df_map,
        "idf_map"      : idf_map,
        "tf_matrix"    : tf_matrix,
        "weight_matrix": weight_matrix,
        "tf_query"     : tf_query,
        "weight_query" : weight_query,
    }
    