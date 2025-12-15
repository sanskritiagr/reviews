import streamlit as st
import utils

st.set_page_config(page_title="Admin Dashboard", layout="wide")
utils.init_storage()

st.title("📊 Admin Dashboard")

# 🔄 Manual refresh button
if st.button("🔄 Refresh Data"):
    st.rerun()

# Read shared data source
df = utils.load_data()

# ---- Analytics ----
col1, col2, col3 = st.columns(3)

col1.metric("Total Reviews", len(df))
col2.metric("Average Rating", round(df["rating"].mean(), 2))
col3.metric("Negative Reviews", len(df[df["rating"] <= 2]))

st.divider()

# ---- Rating Distribution ----
st.subheader("⭐ Rating Distribution")
st.bar_chart(df["rating"].value_counts().sort_index())

# ---- Filters ----
st.subheader("🔍 Filters")

rating_filter = st.selectbox(
    "Filter by Rating",
    options=["All", 1, 2, 3, 4, 5]
)

filtered_df = df
if rating_filter != "All":
    filtered_df = df[df["rating"] == rating_filter]

# ---- Review Table ----
st.subheader("📝 All Submissions")

st.dataframe(
    filtered_df[[
        "timestamp",
        "rating",
        "review",
        "ai_summary",
        "ai_action"
    ]],
    use_container_width=True
)
