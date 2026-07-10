def detect_industry(text):
   

    text = text.lower()

    mapping = {
        "nutrition": [
            "nutrition",
            "protein",
            "supplement",
            "vitamin"
        ],
        "skincare": [
            "skin",
            "beauty",
            "cosmetic"
        ],
        "fitness": [
            "fitness",
            "gym",
            "workout"
        ],
        "health": [
            "health",
            "wellness",
            "care"
        ]
    }

    for industry, words in mapping.items():
        if any(word in text for word in words):
            return industry

    return "unknown"


def qualify_lead(record):
   

    score = 0
    reasons = []

    text = (
        record["Title"] + " " +
        record["Meta Description"]
    ).lower()

    # Active website
    if record["Title"] != "not_available":
        score += 2
        reasons.append("Active website")

    # Industry
    industry = detect_industry(text)

    if industry != "unknown":
        score += 3
        reasons.append("Relevant wellness industry")

    # Product offering
    if any(word in text for word in [
        "product",
        "products",
        "shop",
        "buy",
        "formula",
        "range"
    ]):
        score += 2
        reasons.append("Clear product offering")

    # Marketing activity
    if record.get("blog"):
        score += 2
        reasons.append("Marketing/content activity")

    # Evidence quality
    if len(record["Evidence Snippet"]) > 30:
        score += 1
        reasons.append("Strong public evidence")

    # Lead Status
    if score >= 8:
        status = "qualified"
    elif score >= 5:
        status = "pending_human_review"
    elif score >= 3:
        status = "insufficient_information"
    else:
        status = "not_a_fit"

    # Existing fields
    record["Lead Qualification Score"] = score
    record["Qualification Rationale"] = "; ".join(reasons)
    record["Lead Status"] = status
    record["Industry or Category"] = industry

    # Business Model
    if record.get("ecommerce"):
        business_model = "B2C Ecommerce"
    else:
        business_model = "Unknown"

    record["Business Model"] = business_model

    # Geography
    if ".in" in record["Website URL"]:
        geography = "India"
    else:
        geography = "Global"

    record["Geography or Market Signal"] = geography

    # Contact Route
    record["Public Contact Route"] = (
        "Contact Page"
        if record.get("contact_page")
        else "Website Homepage"
    )

    # ---------- Required Decode Age Fields ----------

    record["Product or Service Type"] = (
        "Products"
        if record.get("ecommerce")
        else "unknown"
    )

    record["Target Audience Signal"] = "Consumers"

    record["Core Product Positioning"] = (
        record["Title"]
        if record["Title"] != "not_available"
        else "unknown"
    )

    record["Key Claims or Messaging"] = (
        record["Meta Description"]
        if record["Meta Description"] != "not_available"
        else "unknown"
    )

    record["E-commerce Signal"] = (
        "Yes"
        if record.get("ecommerce")
        else "No"
    )

    record["Marketing or Content Activity Signal"] = (
        "Active"
        if record.get("blog")
        else "Unknown"
    )

    return record