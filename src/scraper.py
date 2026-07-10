import requests


def fetch_website(url):
    """
    This fetch the HTML content of a website

    Returns:
        status (str)
        status_code (int or None)
        html (str or None)
    """

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/137.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        return "success", response.status_code, response.text

    except requests.exceptions.RequestException:

        return "failed", None, None