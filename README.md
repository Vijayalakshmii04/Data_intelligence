# Decode Age – Data Intelligence Intern Assessment

## Overview

This project is a Python-based lead intelligence pipeline developed for the Decode Age Data Intelligence Intern assessment.

The pipeline starts with a list of companies provided in `seed_companies.csv` and automatically collects publicly available information from their websites. It validates the input data, checks website accessibility, extracts business information, qualifies potential leads using evidence-based scoring, removes duplicates, and exports structured datasets for business review.

The workflow is reusable and can process a new list of company websites without changing the extraction logic.

---

## Project Structure

```
DecodeAge-Assessment/
│
├── data/
│   └── seed_companies.csv
│
├── output/
│   ├── lead_master.csv
│   └── lead_review_queue.csv
│
├── logs/
│
├── src/
│   ├── main.py
│   ├── cleaner.py
│   ├── scraper.py
│   ├── extractor.py
│   ├── qualifier.py
│   ├── exporter.py
│   ├── robots_checker.py
│   ├── deduplicator.py
│   └── utils.py
│
├── workflow_note.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Workflow

The pipeline performs the following steps automatically:

1. Reads the input dataset (`seed_companies.csv`).
2. Validates missing values, duplicate records, and malformed URLs.
3. Downloads each company website using the Requests library.
4. Checks the website's `robots.txt` before collecting data.
5. Extracts publicly available business information using BeautifulSoup.
6. Identifies business signals such as e-commerce indicators, marketing activity, and public contact pages.
7. Qualifies each company using an evidence-based scoring model.
8. Removes duplicate company names and duplicate normalized domains.
9. Exports the processed datasets for business review.

---

## Information Collected

For each company, the pipeline attempts to collect:

- Company Name
- Website URL
- Normalized Domain
- Page Title
- Meta Description
- About Page Availability
- Contact Page Availability
- Careers Page Availability
- Public Social Media Links
- Industry / Category
- Business Model
- Geography Signal
- E-commerce Signal
- Marketing / Content Activity
- Qualification Score
- Qualification Rationale
- Lead Status
- Source URL
- Evidence Snippet
- Collection Date

If information cannot be verified, the pipeline records values such as `unknown` or `not_available` instead of making assumptions.

---

## Lead Qualification

Each company is scored out of **10** using publicly available evidence.

| Qualification Signal | Maximum Score |
|----------------------|--------------:|
| Active Website | 2 |
| Relevant Industry | 3 |
| Product Offering | 2 |
| Marketing / Content Activity | 2 |
| Evidence Quality | 1 |

Lead Status:

- **8–10** → qualified
- **5–7** → pending_human_review
- **3–4** → insufficient_information
- **0–2** → not_a_fit

---

## Libraries Used

- Python 3
- pandas
- requests
- beautifulsoup4
- lxml
- validators
- tldextract
- rapidfuzz
- tqdm
- tenacity

---

## Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate it (Windows)

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run

Execute the pipeline

```bash
python src/main.py
```

The generated CSV files will be saved inside the `output` directory.

---

## Output Files

### lead_master.csv

Contains all processed companies together with extracted information, qualification score, evidence, and lead status.

### lead_review_queue.csv

Contains companies recommended for manual business review.

---

## AI Usage Disclosure

ChatGPT was used to discuss the pipeline design, explain Python concepts, assist with debugging, and improve documentation.

All company information included in the output datasets is collected from publicly accessible sources and manually reviewed during development.

---

## Assumptions

- Only publicly available information is collected.
- No login-protected resources are accessed.
- Missing information is recorded as `unknown` or `not_available`.
- The workflow is designed to be reusable for different company datasets.

---

## Limitations

- Some websites rely heavily on JavaScript, limiting the information available through simple HTTP requests.
- Public information may change over time.
- Final lead qualification should include human review.

---

## Ethical Considerations

This project:

- Uses only publicly available information.
- Does not collect personal data.
- Does not bypass authentication, CAPTCHAs, or access controls.
- Respects robots.txt where checked.
- Records uncertainty instead of inventing missing information.