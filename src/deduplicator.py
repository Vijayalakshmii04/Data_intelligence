import pandas as pd


def remove_duplicate_domains(df):
    

    before = len(df)

    df = df.drop_duplicates(
        subset=["Normalized Domain"],
        keep="first"
    )

    after = len(df)

    print(f"\nDuplicate Domains Removed : {before-after}")

    return df


def remove_duplicate_names(df):
    
    before = len(df)

    df = df.drop_duplicates(
        subset=["Company Name"],
        keep="first"
    )

    after = len(df)

    print(f"Duplicate Company Names Removed : {before-after}")

    return df