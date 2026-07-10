# Workflow Note

## Workflow Overview

```
Seed Companies CSV
        │
        ▼
Load Dataset
        │
        ▼
Validate Dataset
(Missing Values, Duplicate Records, Invalid URLs)
        │
        ▼
Check robots.txt
        │
        ▼
Download Website HTML
        │
        ▼
Extract Public Information
        │
        ▼
Standardize & Normalize Data
        │
        ▼
Deduplicate Records
        │
        ▼
Lead Qualification
        │
        ▼
Export lead_master.csv
        │
        ▼
Export lead_review_queue.csv
```

---

## 1. Data Collection

The workflow begins by reading the provided `seed_companies.csv` file.

Each website URL is validated before an HTTP request is made using the Python Requests library with a custom User-Agent.

Before collecting information, the pipeline checks whether the homepage is allowed by the website's `robots.txt`. Only publicly accessible pages are processed.

---

## 2. Information Extraction

Website HTML is parsed using BeautifulSoup.

The pipeline extracts publicly available information including:

- Page title
- Meta description
- About page availability
- Contact page availability
- Careers page availability
- Public social media links
- E-commerce indicators
- Marketing/content indicators

The extracted information is stored in a structured format for further processing.

---

## 3. Data Standardization

The pipeline standardizes website domains using domain normalization.

It validates malformed URLs, detects missing values, and records unavailable information using values such as `unknown` or `not_available` instead of making assumptions.

Duplicate company names and duplicate normalized domains are removed before exporting the final datasets.

---

## 4. Lead Qualification

Each company is evaluated using an evidence-based scoring model with a maximum score of 10.

The scoring considers:

- Active website
- Relevant industry
- Product offering
- Marketing or content activity
- Strength of public evidence

Based on the final score, companies are classified as:

- qualified
- pending_human_review
- insufficient_information
- not_a_fit

Each qualification is supported by publicly available evidence extracted from the company website.

---

## 5. Evidence and Confidence

Every lead retains:

- Source URL
- Evidence snippet
- Collection date
- Qualification rationale
- Confidence level

When sufficient information is unavailable, the workflow records the uncertainty rather than generating unsupported conclusions.

---

## 6. Error Handling

The pipeline handles common data collection issues including:

- Invalid website URLs
- Failed HTTP requests
- Missing HTML elements
- Duplicate records
- Restricted pages identified through robots.txt
- Missing or incomplete public information

The workflow continues processing remaining companies even if one website cannot be accessed.

---

## Reusability

The workflow is fully reusable.

To process another batch of companies, only the input CSV file needs to be replaced. No changes to the extraction or qualification logic are required.

The output files (`lead_master.csv` and `lead_review_queue.csv`) are generated automatically for each run.