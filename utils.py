import pandas as pd
import os

DATA_FILE = "reviews.csv"

REQUIRED_COLUMNS = [
    "timestamp",
    "rating",
    "review",
    "ai_response",
    "ai_summary",
    "ai_action"
]

def init_storage():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=REQUIRED_COLUMNS)
        df.to_csv(DATA_FILE, index=False)
        return

    df = pd.read_csv(DATA_FILE)

    # 🔧 Add missing columns safely
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            df[col] = ""

    df = df[REQUIRED_COLUMNS]  # enforce order
    df.to_csv(DATA_FILE, index=False)


def load_data():
    return pd.read_csv(DATA_FILE)


def save_data(df):
    df.to_csv(DATA_FILE, index=False)


# ---- AI helpers ----
def ai_summary(review):
    return review[:80] + "..." if len(review) > 80 else review

def ai_action(rating):
    if rating >= 4:
        return "No action needed"
    elif rating == 3:
        return "Monitor feedback"
    else:
        return "Escalate to support"
