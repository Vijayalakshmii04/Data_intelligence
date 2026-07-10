import validators


def validate_dataset(df):
    """
    Validate the input dataset before web scraping.
    """

    print("\n========== DATA VALIDATION ==========\n")

    # ---------------------------------
    # Check missing values
    # ---------------------------------
    print("Checking missing values...")

    missing_values = df.isnull().sum()

    print(missing_values)

    # ---------------------------------
    # Check duplicate rows
    # ---------------------------------
    print("\nChecking duplicate rows...")

    duplicate_rows = df.duplicated().sum()

    print(f"Duplicate rows found: {duplicate_rows}")

    # ---------------------------------
    # Check invalid URLs
    # ---------------------------------
    print("\nChecking website URLs...\n")

    invalid_urls = []

    for index, row in df.iterrows():

        url = row["website_url"]

        if not validators.url(url):

            invalid_urls.append(
                {
                    "row": index,
                    "company": row["company_name"],
                    "url": url,
                }
            )

    if len(invalid_urls) == 0:

        print("All URLs are valid.")

    else:

        print("Invalid URLs Found:\n")

        for item in invalid_urls:

            print(item)

    print("\nValidation Completed.\n")

    return df