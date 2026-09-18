import pandas as pd

data = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    }
]

faq_df = pd.DataFrame(data)

def score_query(query, df):

    query_words = query.lower().split()

    results = []

    for _, row in df.iterrows():

        score = 0

        for word in query_words:

            if word in row["question"].lower():
                score += 2

            if word in row["keywords"].lower():
                score += 1

        if score > 0:
            results.append({
                "question": row["question"],
                "score": score
            })

    return sorted(results,
                  key=lambda x: x["score"],
                  reverse=True)

print(score_query("fee payment", faq_df))