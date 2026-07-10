from urllib.parse import urlparse


def get_normalized_domain(url):
    
    

    try:

        parsed = urlparse(url)

        domain = parsed.netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        return domain

    except Exception:

        return "unknown"