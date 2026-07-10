import pandas as pd

from cleaner import validate_dataset
from scraper import fetch_website
from extractor import extract_basic_info
from robots_checker import check_robots
from exporter import export_lead_master
from datetime import datetime
from qualifier import qualify_lead
from utils import get_normalized_domain
from deduplicator import (
    remove_duplicate_domains,
    remove_duplicate_names
)
from exporter import (
    export_lead_master,
    export_review_queue
)


def main():

    csv_path = "data/seed_companies.csv"

    df = pd.read_csv(csv_path)

    print("Dataset Loaded Successfully")
    print(f"Total Companies: {len(df)}")

    validate_dataset(df)

    

    records = []

    for _, row in df.iterrows():

        company = row["company_name"]
        website = row["website_url"]

        print(f"\nProcessing: {company}")

        status, code, html = fetch_website(website)

        if status != "success":

            print(f"Website could not be reached: {website}")

            records.append({
                "Lead ID": row["seed_id"],
                "Company Name": company,
                "Website URL": website,
                "Title": "not_available",
                "Meta Description": "not_available",
                "Source URL": website,
                "Evidence Snippet": "",
                "Collection Date": datetime.today().strftime("%Y-%m-%d"),
                "Lead Status": "needs_human_review"
            })

            continue

        info = extract_basic_info(html)

        robots = check_robots(website)

        print(f"Status Code : {code}")
        print(f"Robots Allowed : {robots['allowed']}")

        record = {
            "Lead ID": row["seed_id"],
            "Company Name": company,
            "Website URL": website,
            "Normalized Domain": get_normalized_domain(website),
            "Title": info["title"],
            "Meta Description": info["meta_description"],
            "Source URL": website,
            "Evidence Snippet": info["meta_description"][:200],
            "Collection Date": datetime.today().strftime("%Y-%m-%d"),
            "Lead Status": "pending_human_review",
            "Data Confidence": "High" if status == "success" else "Low"
        }
        record = qualify_lead(record)
        records.append(record)
       

    lead_df = pd.DataFrame(records)

    lead_df = remove_duplicate_names(lead_df)

    lead_df = remove_duplicate_domains(lead_df)

    records = lead_df.to_dict("records")

    export_lead_master(records)
    export_review_queue(records)

    print("\n---------- EXTRACTED INFORMATION ----------\n")

    for key, value in info.items():
        print(f"{key:20}: {value}")

        robots = check_robots(website)

        print("\n---------- ROBOTS.TXT ----------\n")

        print(f"Robots URL   : {robots['robots_url']}")
        print(f"Found        : {robots['robots_found']}")
        print(f"Allowed      : {robots['allowed']}")

        if robots["error"]:
            print(f"Error        : {robots['error']}")


if __name__ == "__main__":
    main()