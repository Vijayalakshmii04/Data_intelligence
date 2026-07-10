from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser


def check_robots(website_url):
  

    result = {
        "robots_found": False,
        "allowed": False,
        "robots_url": "",
        "error": ""
    }

    try:

        robots_url = urljoin(website_url, "/robots.txt")

        rp = RobotFileParser()

        rp.set_url(robots_url)

        rp.read()

        result["robots_found"] = True
        result["robots_url"] = robots_url
        result["allowed"] = rp.can_fetch("*", website_url)

    except Exception as e:

        result["error"] = str(e)

    return result