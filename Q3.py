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
def same_category(category_name, df):

    return df[df["category"] == category_name]


print(same_category("billing", faq_df))