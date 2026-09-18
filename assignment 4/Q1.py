import pandas as pd 
ROLL_NUMBER = "1024170113"  

fixed_entries = [
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
    }
]

categories = ["billing", "account", "general"]

last_three_digits = [int(d) for d in ROLL_NUMBER[-3:]]

generated_entries = []

for digit in last_three_digits[:2]:
    category = categories[digit % 3]

    if category == "billing":
        generated_entries.append({
            "question": "can i get a fee receipt",
            "answer": "Yes, you can download the fee receipt from the student portal.",
            "keywords": "fee receipt payment download",
            "category": "billing"
        })

    elif category == "account":
        generated_entries.append({
            "question": "how do i update my registered mobile number",
            "answer": "Go to Profile Settings and update your mobile number.",
            "keywords": "mobile number update profile",
            "category": "account"
        })

    else:
        generated_entries.append({
            "question": "where is the college located",
            "answer": "The college is located in Patiala, Punjab.",
            "keywords": "college location address",
            "category": "general"
        })

faq_df = pd.DataFrame(fixed_entries + generated_entries)

print("===== FINAL FAQ DATAFRAME =====")
print(faq_df)