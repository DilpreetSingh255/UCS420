import pandas as pd

faq_data = [
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
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    },
    {
        "question": "how do i update my mobile number",
        "answer": "Update it through Profile Settings.",
        "keywords": "mobile number profile update",
        "category": "account"
    },
    {
        "question": "where is the college located",
        "answer": "The college is located in Patiala.",
        "keywords": "college location address",
        "category": "general"
    }
]

faq_df = pd.DataFrame(faq_data)
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


def best_match(query, df):

    result = score_query(query, df)

    if not result:
        print("No Match Found")
        return

    highest_score = result[0]["score"]

    print("Highest Score =", highest_score)

    for item in result:
        if item["score"] == highest_score:
            print(item)


print("Tie Example:")
best_match("fee", faq_df)

print("\nNon-Tie Example:")
best_match("password reset", faq_df)