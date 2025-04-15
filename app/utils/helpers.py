# app/utils/helpers.py
def is_tenancy_question(message: str) -> bool:
    keywords = ["rent", "landlord", "deposit", "notice", "evict", "contract", "tenancy", "agreement"]
    return any(word in message.lower() for word in keywords)
