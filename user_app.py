import streamlit as st
from datetime import datetime
import utils

utils.init_storage()

st.title("⭐ User Review Dashboard")

rating = st.slider("Select Rating", 1, 5, 5)
review = st.text_area("Write a short review", max_chars=300)

if st.button("Submit"):
    if review.strip() == "":
        st.warning("Review cannot be empty")
    else:
        df = utils.load_data()

        row = {
            "timestamp": datetime.now().isoformat(),
            "rating": rating,
            "review": review,
            "ai_response": "Thank you for your feedback!",
            "ai_summary": utils.ai_summary(review),
            "ai_action": utils.ai_action(rating)
        }

        df.loc[len(df)] = row
        utils.save_data(df)

        st.success("Submitted successfully!")
        st.write("🤖 AI Response:")
        st.write(row["ai_response"])
