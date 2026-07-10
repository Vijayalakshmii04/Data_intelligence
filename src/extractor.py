from bs4 import BeautifulSoup


def extract_basic_info(html): #this extraccts useful business info
    
    
    
    soup = BeautifulSoup(html, "lxml")

    result = {
        "title": "",
        "meta_description": "",
        "about_page": False,
        "contact_page": False,
        "careers_page": False,
        "linkedin": "",
        "instagram": "",
        "facebook": "",
        "youtube": ""
    }

    # Title
    if soup.title:
        result["title"] = soup.title.get_text(strip=True)

    # Meta Description
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content"):
        result["meta_description"] = meta["content"].strip()

    # Find Links
    for link in soup.find_all("a", href=True):

        href = link["href"]
        href_lower = href.lower()

        text = link.get_text(" ", strip=True).lower()

        # About
        if "about" in href_lower or "about" in text:
            result["about_page"] = True

        # Contact
        if "contact" in href_lower or "contact" in text:
            result["contact_page"] = True

        # Careers
        if (
            "career" in href_lower
            or "jobs" in href_lower
            or "career" in text
            or "jobs" in text
        ):
            result["careers_page"] = True

        # Social Media
        if "linkedin.com" in href_lower:
            result["linkedin"] = href

        elif "instagram.com" in href_lower:
            result["instagram"] = href

        elif "facebook.com" in href_lower:
            result["facebook"] = href

        elif "youtube.com" in href_lower or "youtu.be" in href_lower:
            result["youtube"] = href

    # Detect e-commerce keywords
    page_text = soup.get_text(" ", strip=True).lower()

    result["ecommerce"] = any(
        word in page_text
        for word in [
            "add to cart",
            "buy now",
            "shop",
            "checkout",
            "cart"
        ]
)

    # Detect marketing/content activity
    result["blog"] = (
        "blog" in page_text or
        "articles" in page_text or
        "news" in page_text
    )
    return result