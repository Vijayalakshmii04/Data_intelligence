import os
import pandas as pd


OUTPUT_FOLDER = "output"


def export_lead_master(records):
    
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "lead_master.csv"
    )

    df = pd.DataFrame(records)

    df.to_csv(output_file, index=False)

    print(f"\nLead Master Saved -> {output_file}")

    return output_file


def export_review_queue(records):
   
    #Save only leads requiring business review.
   

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "lead_review_queue.csv"
    )

    df = pd.DataFrame(records)

    df.to_csv(output_file, index=False)

    print(f"Review Queue Saved -> {output_file}")

    return output_file
def export_review_queue(records):
    
    #Export only qualified or pending review leads.
    

    review_records = []

    for record in records:

        if record["Lead Status"] in [
            "qualified",
            "pending_human_review"
        ]:

            review_records.append({
                "Company Name": record["Company Name"],
                "Website": record["Website URL"],
                "Qualification Score": record["Lead Qualification Score"],
                "Why It Is Relevant": record["Qualification Rationale"],
                "Evidence Source": record["Source URL"],
                "Confidence": record["Data Confidence"],
                "Recommended Next Step": "Business Review",
                "Review Status": "pending_review"
            })

    output_file = "output/lead_review_queue.csv"

    pd.DataFrame(review_records).to_csv(
        output_file,
        index=False
    )

    print(f"Review Queue Saved -> {output_file}")